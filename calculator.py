"""
영양성분 자동 계산 엔진
- 배합비 × 원재료 영양성분 DB → 제품별 9대 영양성분
"""
from ingredient_db import INGREDIENT_DB, NUTRIENT_KEYS, NUTRIENT_LABELS, normalize_name, get_nutrient
from food_db_extended import EXTENDED_DB


def calculate_nutrition(ingredients, serving_size_g=None):
    """
    제품 영양성분 계산

    Args:
        ingredients: [(원재료명, 투입량g), ...]
        serving_size_g: 1회 제공량(g). None이면 총중량 기준

    Returns:
        dict with:
            - per_total: 총중량 기준 영양성분
            - per_100g: 100g당 영양성분
            - per_serving: 1회 제공량 기준 (serving_size_g 지정 시)
            - total_weight: 총 배합 중량(g)
            - mapped_weight: DB 매핑된 원재료 중량(g)
            - unmapped: 미매핑 원재료 리스트
            - coverage: 매핑률(%)
    """
    total_weight = sum(qty for _, qty in ingredients)
    if total_weight == 0:
        return None

    # 영양성분 합산 (총중량 기준)
    nutrition_total = {k: 0.0 for k in NUTRIENT_KEYS}
    mapped_weight = 0
    unmapped = []

    # 학습 DB 로드
    try:
        from auto_lookup import load_learned_db
        learned_db = load_learned_db()
    except ImportError:
        learned_db = {}

    for name, qty in ingredients:
        norm = normalize_name(name)
        nutrient = get_nutrient(norm)

        # 기본 DB에 없으면 확장 DB 확인
        if nutrient is None:
            nutrient = EXTENDED_DB.get(name) or EXTENDED_DB.get(norm)

        # 확장 DB에도 없으면 학습 DB 확인
        if nutrient is None and name in learned_db:
            nutrient = learned_db[name].get("nutrition")
        if nutrient is None and norm in learned_db:
            nutrient = learned_db[norm].get("nutrition")

        if nutrient is None:
            unmapped.append((name, qty))
            continue

        mapped_weight += qty
        ratio = qty / 100.0  # DB는 100g당 기준

        for key in NUTRIENT_KEYS:
            nutrition_total[key] += nutrient[key] * ratio

    # 100g당 환산
    nutrition_per_100g = {}
    for key in NUTRIENT_KEYS:
        nutrition_per_100g[key] = round(nutrition_total[key] / total_weight * 100, 2)

    # 총중량 기준 반올림
    for key in NUTRIENT_KEYS:
        nutrition_total[key] = round(nutrition_total[key], 2)

    # 1회 제공량 기준
    nutrition_per_serving = None
    if serving_size_g:
        nutrition_per_serving = {}
        for key in NUTRIENT_KEYS:
            nutrition_per_serving[key] = round(nutrition_per_100g[key] * serving_size_g / 100, 2)

    coverage = (mapped_weight / total_weight * 100) if total_weight > 0 else 0

    return {
        "per_total": nutrition_total,
        "per_100g": nutrition_per_100g,
        "per_serving": nutrition_per_serving,
        "total_weight": total_weight,
        "mapped_weight": mapped_weight,
        "unmapped": unmapped,
        "coverage": round(coverage, 1),
    }


def format_nutrition_label(result, product_name="", serving_size_g=None):
    """영양성분 표시 형식으로 출력"""
    lines = []
    lines.append("=" * 50)
    lines.append(f"  영양성분 정보 {'- ' + product_name if product_name else ''}")
    lines.append("=" * 50)

    basis = result["per_100g"]
    lines.append(f"\n  ■ 100g당")
    lines.append(f"  {'─' * 40}")

    # 1일 영양소 기준치
    daily = {
        "kcal": 2000, "carb": 324, "sugar": 100, "protein": 55,
        "fat": 54, "sat_fat": 15, "trans_fat": None,
        "cholesterol": 300, "sodium": 2000
    }

    for key in NUTRIENT_KEYS:
        label = NUTRIENT_LABELS[key]
        val = basis[key]
        dv = daily.get(key)
        if dv:
            pct = round(val / dv * 100)
            lines.append(f"  {label:20s} {val:>8.1f}  ({pct}%)")
        else:
            lines.append(f"  {label:20s} {val:>8.1f}")

    if serving_size_g and result["per_serving"]:
        lines.append(f"\n  ■ 1회 제공량 ({serving_size_g}g)당")
        lines.append(f"  {'─' * 40}")
        serving = result["per_serving"]
        for key in NUTRIENT_KEYS:
            label = NUTRIENT_LABELS[key]
            val = serving[key]
            dv = daily.get(key)
            if dv:
                pct = round(val / dv * 100)
                lines.append(f"  {label:20s} {val:>8.1f}  ({pct}%)")
            else:
                lines.append(f"  {label:20s} {val:>8.1f}")

    lines.append(f"\n  ■ 배합 정보")
    lines.append(f"  {'─' * 40}")
    lines.append(f"  총 배합 중량:     {result['total_weight']:.0f}g")
    lines.append(f"  DB 매핑 중량:     {result['mapped_weight']:.0f}g")
    lines.append(f"  매핑률:           {result['coverage']:.1f}%")

    if result["unmapped"]:
        lines.append(f"\n  ⚠ 미매핑 원재료 ({len(result['unmapped'])}건):")
        for name, qty in result["unmapped"]:
            lines.append(f"    - {name}: {qty:.1f}g ({qty/result['total_weight']*100:.1f}%)")

    lines.append("=" * 50)
    return "\n".join(lines)


if __name__ == "__main__":
    # 테스트: 간단한 통밀식빵 배합
    test_recipe = [
        ("통밀가루", 500),
        ("정제수", 350),
        ("현미유", 30),
        ("하얀설탕", 20),
        ("정제소금", 8),
        ("드라이이스트", 5),
    ]

    result = calculate_nutrition(test_recipe, serving_size_g=100)
    print(format_nutrition_label(result, "테스트 통밀식빵", 100))
