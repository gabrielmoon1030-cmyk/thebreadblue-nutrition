"""
배합비 Excel 파서
- 배합비 폴더에서 원재료명 + 투입량(g) 자동 추출
- 다양한 엑셀 형식 대응 (레시피/원가 파일)
"""
import re
import openpyxl
from pathlib import Path
from ingredient_db import normalize_name

# 로컬 전용 (클라우드에서는 파일 업로드 모드만 사용)
_local_recipe_dir = r"C:\Users\Moon\OneDrive\03. 양지희_품질\7. 배합비"
RECIPE_DIR = Path(_local_recipe_dir) if Path(_local_recipe_dir).exists() else None


def parse_recipe_file(filepath):
    """단일 배합비 Excel에서 (제품명, [(원재료, 투입량g), ...]) 추출"""
    results = []
    try:
        wb = openpyxl.load_workbook(filepath, read_only=True, data_only=True)
    except Exception as e:
        return []

    for ws in wb.worksheets:
        sheet_name = ws.title
        # '품목' 시트는 라벨용 재정렬이므로 스킵
        if '품목' in sheet_name:
            continue

        # 제품명 추출 (보통 B1 또는 B2)
        product_name = None
        for row_num in range(1, 4):
            cell_b = ws.cell(row=row_num, column=2).value
            if cell_b and isinstance(cell_b, str) and len(cell_b.strip()) > 1:
                val = cell_b.strip()
                if not any(k in val for k in ['단위', '규격', '원재료', '배합']):
                    product_name = val
                    break

        if not product_name:
            product_name = Path(filepath).stem

        # 원재료 + 투입량 추출
        ingredients = []
        header_row = None

        # 헤더 행 찾기 (원재료 컬럼)
        for row_num in range(1, 10):
            cell_a = ws.cell(row=row_num, column=1).value
            if cell_a and '원재료' in str(cell_a):
                header_row = row_num
                break

        if header_row is None:
            continue

        # 투입량 컬럼 찾기 (1배합 또는 다음 숫자 컬럼)
        qty_col = 2  # 기본값: B열
        for col in range(2, 8):
            cell = ws.cell(row=header_row, column=col).value
            if cell and ('1배합' in str(cell) or '배합' in str(cell)):
                qty_col = col
                break

        # 데이터 읽기
        for row_num in range(header_row + 1, 60):
            cell_a = ws.cell(row=row_num, column=1).value
            cell_qty = ws.cell(row=row_num, column=qty_col).value

            if cell_a is None:
                continue

            name = str(cell_a).strip()

            # 종료 조건
            if any(k in name for k in ['합계', 'MEMO', 'memo', '소계', '총합', '개당', '판매']):
                break

            # 필터
            if len(name) < 2:
                continue
            if re.match(r'^[\d.,\s%()]+$', name):
                continue

            # 공정 지시어 제외 (실제 원재료명은 통과시킴)
            skip_keywords = ['반죽', '성형', '굽기', '냉각', '분할', '℃', '오븐',
                           '뚜껑', '모양', '올려', '넣어', '섞어', '비고',
                           '단위', '규격', '입고', '원가', '백분율', '제품명']
            # '글루텐 60%' 같은 공정 메모는 제외하되, '활성밀글루텐' 같은 원재료는 통과
            if any(k in name for k in skip_keywords):
                continue
            if re.search(r'글루텐\s*\d', name) or name == '글루텐':
                continue

            # 투입량 파싱
            qty = 0
            if cell_qty is not None:
                try:
                    qty = float(cell_qty)
                except (ValueError, TypeError):
                    # 문자열에서 숫자 추출 시도
                    match = re.search(r'[\d.]+', str(cell_qty))
                    if match:
                        qty = float(match.group())

            if qty > 0:
                norm_name = normalize_name(name)
                ingredients.append((norm_name, qty))

        if ingredients:
            results.append({
                "product_name": product_name,
                "sheet_name": sheet_name,
                "file": str(filepath),
                "ingredients": ingredients,
                "total_weight": sum(q for _, q in ingredients)
            })

    wb.close()
    return results


def parse_all_recipes():
    """전체 배합비 폴더 파싱 (로컬 전용)"""
    if RECIPE_DIR is None or not RECIPE_DIR.exists():
        return []
    all_recipes = []
    xlsx_files = list(RECIPE_DIR.rglob("*.xlsx"))

    for fpath in xlsx_files:
        if "~$" in fpath.name:
            continue
        recipes = parse_recipe_file(fpath)
        all_recipes.extend(recipes)

    # 중복 제거 (같은 제품명이면 가장 최근 파일 우선)
    seen = {}
    for r in all_recipes:
        key = r["product_name"]
        if key not in seen:
            seen[key] = r
        # 나중에 파싱된 것이 더 최근 → 덮어쓰기

    return list(seen.values())


if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding='utf-8')

    recipes = parse_all_recipes()
    print(f"총 {len(recipes)}개 레시피 파싱 완료\n")

    for r in recipes[:5]:
        print(f"[{r['product_name']}] (총 {r['total_weight']:.0f}g)")
        for name, qty in r['ingredients'][:8]:
            print(f"  - {name}: {qty:.1f}g")
        if len(r['ingredients']) > 8:
            print(f"  ... 외 {len(r['ingredients'])-8}건")
        print()
