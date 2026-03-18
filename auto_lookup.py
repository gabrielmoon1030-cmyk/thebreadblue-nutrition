"""
미매핑 원재료 자동 검색/학습 모듈
1. 로컬 DB에 없는 원재료 → 유사명칭 자동 검색
2. 식약처 API 검색 (API키 있을 때)
3. 사용자가 확인/수정하면 학습 DB에 저장 → 다음부터 자동 인식
"""
import json
import os
import re
import urllib.request
import urllib.parse
from pathlib import Path
from difflib import SequenceMatcher
from ingredient_db import INGREDIENT_DB, NUTRIENT_KEYS, normalize_name
from food_db_extended import EXTENDED_DB

BASE_DIR = Path(__file__).parent
LEARNED_DB_PATH = BASE_DIR / "data" / "learned_ingredients.json"
API_KEY_PATH = BASE_DIR / "data" / "api_key.txt"

# ============================================================
# 1. 학습된 원재료 DB (사용자가 확인한 매핑)
# ============================================================
def load_learned_db():
    """학습된 원재료 DB 로드"""
    if LEARNED_DB_PATH.exists():
        with open(LEARNED_DB_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_learned_db(db):
    """학습된 원재료 DB 저장"""
    LEARNED_DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(LEARNED_DB_PATH, "w", encoding="utf-8") as f:
        json.dump(db, f, ensure_ascii=False, indent=2)

def add_learned_ingredient(name, nutrition_data, source="manual"):
    """
    새 원재료를 학습 DB에 추가
    nutrition_data: {"kcal": ..., "carb": ..., ...}
    source: "manual", "api", "similar"
    """
    db = load_learned_db()
    db[name] = {
        "nutrition": nutrition_data,
        "source": source,
    }
    save_learned_db(db)
    return True


# ============================================================
# 2. 유사명칭 검색 (로컬 DB 내 fuzzy match)
# ============================================================
def find_similar_ingredients(query, top_n=5, threshold=0.4):
    """
    로컬 DB + 학습 DB에서 유사한 원재료명 검색
    Returns: [(이름, 유사도점수, 영양성분dict), ...]
    """
    all_names = {}

    # 기본 DB
    for name, nutr in INGREDIENT_DB.items():
        all_names[name] = nutr

    # 확장 DB (식약처 식품성분표 기반)
    for name, nutr in EXTENDED_DB.items():
        if name not in all_names:
            all_names[name] = nutr

    # 학습 DB
    learned = load_learned_db()
    for name, data in learned.items():
        all_names[name] = data["nutrition"]

    results = []
    query_norm = query.strip()

    for name, nutr in all_names.items():
        # 여러 유사도 방식 조합
        score = 0

        # 1. 완전 포함
        if query_norm in name or name in query_norm:
            score = max(score, 0.8)

        # 2. SequenceMatcher
        seq_score = SequenceMatcher(None, query_norm, name).ratio()
        score = max(score, seq_score)

        # 3. 공통 글자 비율
        common = len(set(query_norm) & set(name))
        char_score = common / max(len(set(query_norm)), len(set(name)), 1)
        score = max(score, char_score * 0.7)

        # 4. 키워드 매칭 (가루, 분말, 유, 버터 등)
        keywords = ['가루', '분말', '파우더', '유', '버터', '크림', '설탕', '초콜릿', '소금']
        for kw in keywords:
            if kw in query_norm and kw in name:
                score = max(score, 0.5)

        if score >= threshold:
            results.append((name, round(score, 3), nutr))

    results.sort(key=lambda x: -x[1])
    return results[:top_n]


# ============================================================
# 3. 식약처 API 검색 (API키 필요)
# ============================================================
def get_api_key():
    """저장된 API키 로드"""
    if API_KEY_PATH.exists():
        return API_KEY_PATH.read_text(encoding="utf-8").strip()
    return None

def save_api_key(key):
    """API키 저장"""
    API_KEY_PATH.parent.mkdir(parents=True, exist_ok=True)
    API_KEY_PATH.write_text(key.strip(), encoding="utf-8")

def search_foodsafety_api(keyword, max_results=10):
    """
    식품안전나라 I2790 API로 검색
    Returns: [{"name": ..., "nutrition": {...}, "category": ..., "maker": ...}, ...]
    """
    api_key = get_api_key()
    if not api_key:
        return None  # API키 없음

    encoded_keyword = urllib.parse.quote(keyword)
    url = f"http://openapi.foodsafetykorea.go.kr/api/{api_key}/I2790/json/1/{max_results}/DESC_KOR={encoded_keyword}"

    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=10) as resp:
            raw = resp.read().decode("utf-8")
            # HTML 응답 (인증 오류 등) 무시
            if raw.strip().startswith("<"):
                return []
            data = json.loads(raw)

        if "I2790" not in data:
            return []

        result_data = data["I2790"]
        if "RESULT" in result_data and result_data["RESULT"].get("CODE") != "INFO-000":
            return []

        rows = result_data.get("row", [])
        results = []

        for row in rows:
            def safe_float(val):
                if not val or val == "-" or val == "N/A" or val == "":
                    return 0.0
                try:
                    return float(str(val).replace(",", ""))
                except ValueError:
                    return 0.0

            nutrition = {
                "kcal": safe_float(row.get("NUTR_CONT1", 0)),
                "carb": safe_float(row.get("NUTR_CONT2", 0)),
                "protein": safe_float(row.get("NUTR_CONT3", 0)),
                "fat": safe_float(row.get("NUTR_CONT4", 0)),
                "sugar": safe_float(row.get("NUTR_CONT5", 0)),
                "sodium": safe_float(row.get("NUTR_CONT6", 0)),
                "cholesterol": safe_float(row.get("NUTR_CONT7", 0)),
                "sat_fat": safe_float(row.get("NUTR_CONT8", 0)),
                "trans_fat": safe_float(row.get("NUTR_CONT9", 0)),
            }

            serving_size = row.get("SERVING_SIZE", "100")
            try:
                serving_g = float(str(serving_size).replace("g", "").replace(",", "").strip())
            except ValueError:
                serving_g = 100

            # 100g당으로 환산
            if serving_g > 0 and serving_g != 100:
                for key in nutrition:
                    nutrition[key] = round(nutrition[key] / serving_g * 100, 2)

            results.append({
                "name": row.get("DESC_KOR", ""),
                "nutrition": nutrition,
                "category": row.get("GROUP_NAME", ""),
                "maker": row.get("MAKER_NAME", ""),
                "serving_size": serving_size,
            })

        return results

    except Exception as e:
        return None


# ============================================================
# 4. 통합 검색 함수
# ============================================================
def lookup_ingredient(name):
    """
    원재료 영양성분 통합 검색
    1. 기본 DB 확인
    2. 학습 DB 확인
    3. 유사명칭 검색
    4. 식약처 API 검색

    Returns: {
        "found": True/False,
        "source": "local_db" | "learned_db" | "similar" | "api" | None,
        "nutrition": {...} or None,
        "suggestions": [...] (유사명칭/API 결과)
    }
    """
    norm = normalize_name(name)

    # 1. 기본 DB
    if norm in INGREDIENT_DB:
        return {
            "found": True,
            "source": "local_db",
            "nutrition": INGREDIENT_DB[norm],
            "matched_name": norm,
            "suggestions": []
        }

    # 2. 학습 DB
    learned = load_learned_db()
    if name in learned:
        return {
            "found": True,
            "source": "learned_db",
            "nutrition": learned[name]["nutrition"],
            "matched_name": name,
            "suggestions": []
        }
    if norm in learned:
        return {
            "found": True,
            "source": "learned_db",
            "nutrition": learned[norm]["nutrition"],
            "matched_name": norm,
            "suggestions": []
        }

    # 2.5. 확장 DB (식약처 식품성분표)
    if name in EXTENDED_DB:
        return {
            "found": True,
            "source": "extended_db",
            "nutrition": EXTENDED_DB[name],
            "matched_name": name,
            "suggestions": []
        }
    if norm in EXTENDED_DB:
        return {
            "found": True,
            "source": "extended_db",
            "nutrition": EXTENDED_DB[norm],
            "matched_name": norm,
            "suggestions": []
        }

    # 3. 유사명칭 검색 (기본DB + 확장DB + 학습DB 모두 포함)
    similar = find_similar_ingredients(name)

    # 4. 식약처 API
    api_results = search_foodsafety_api(name)

    suggestions = []

    # 유사명칭 결과
    for s_name, s_score, s_nutr in similar:
        suggestions.append({
            "name": s_name,
            "score": s_score,
            "nutrition": s_nutr,
            "source": "similar",
        })

    # API 결과
    if api_results:
        for ar in api_results:
            suggestions.append({
                "name": ar["name"],
                "score": 0,  # API는 score 없음
                "nutrition": ar["nutrition"],
                "source": "api",
                "category": ar.get("category", ""),
                "maker": ar.get("maker", ""),
            })

    return {
        "found": False,
        "source": None,
        "nutrition": None,
        "matched_name": None,
        "suggestions": suggestions,
    }


if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")

    test_names = ["활성밀글루텐", "코코넛슈레드", "쿠킹크림", "자색고구마분말", "프로틴파우더"]

    for name in test_names:
        print(f"\n=== {name} ===")
        result = lookup_ingredient(name)
        if result["found"]:
            print(f"  ✅ 찾음 ({result['source']}): {result['matched_name']}")
        else:
            print(f"  ❌ DB에 없음")
            if result["suggestions"]:
                print(f"  📋 유사 추천:")
                for s in result["suggestions"][:3]:
                    src = "DB유사" if s["source"] == "similar" else "식약처API"
                    print(f"    - {s['name']} (유사도:{s['score']:.2f}, {src})")
                    n = s["nutrition"]
                    print(f"      열량:{n['kcal']}kcal 탄:{n['carb']}g 단:{n['protein']}g 지:{n['fat']}g 나:{n['sodium']}mg")
