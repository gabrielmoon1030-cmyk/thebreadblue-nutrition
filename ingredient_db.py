"""
더브레드블루 원재료 영양성분 데이터베이스
- 100g당 9대 영양성분 기준
- 출처: 식품안전나라, 농촌진흥청 국가표준식품성분표
필드: kcal, carb, sugar, protein, fat, sat_fat, trans_fat, cholesterol, sodium
"""

# 원재료명 정규화 맵 (오타, 변형, 동의어 → 표준명)
NORMALIZE_MAP = {
    # 오타 수정
    '햐안설탕': '하얀설탕', '흥국쌀가루': '홍국쌀가루', '흥국적색소': '홍국적색소',
    '발력쌀가루': '박력쌀가루', '제방전용분': '제빵전용분',
    # 동의어/변형
    '앤지마띠꼬': '엔지마띠코', '엔지마띠꼬': '엔지마띠코', '앤지마띠코': '엔지마띠코', '엔지마끼꼬': '엔지마띠코',
    '크렌베리': '크랜베리', '데코젤미루와': '데코젤미로와',
    '유기농블록': '유기농블락', '유기농 비건블록': '유기농비건블록', '유기농비건블락': '유기농비건블록',
    '유기농블럭': '유기농블락',
    # 밀가루 변형
    '통밀가루M': '통밀가루', '통밀가루강력M': '통밀가루', '통밀가루강력': '통밀가루',
    '우리밀통밀가루': '통밀가루', '우리밀': '제빵전용분',
    '박력밀가루': '박력분', '강력밀가루': '제빵전용분',
    '강력 쌀가루': '강력쌀가루',
    # 설탕/감미료
    '알룰로스': '알룰로오스',
    '프락토 올리고당': '올리고당', '프락토올리고당': '올리고당',
    # 유지
    '올리브오일': '올리브유', '쌀눈유': '현미유',
    # 견과
    '백아몬드분말': '아몬드분말', '아몬드파우더': '아몬드분말', '백아분말': '아몬드분말',
    '피넛버터': '땅콩버터',
    # 유제품
    '식물성휘핑크림': '식물성크림', '엑설런스휘핑크림': '식물성크림',
    # 기타
    '코코아분말': '코코아파우더', '레몬주스': '레몬즙',
    '베이킹파우더(프리)': '베이킹파우더',
    '소금': '정제소금',
    '검정깨': '참깨', '검은깨': '참깨',
    '다진마늘': '마늘',
    '콘스타치': '옥수수전분',
    '타피오카': '타피오카전분',
}

def normalize_name(name):
    name = str(name).strip()
    return NORMALIZE_MAP.get(name, name)


# 100g당 영양성분 DB
INGREDIENT_DB = {
    # ============================================================
    # 밀가루/곡물가루
    # ============================================================
    "제빵전용분":       {"kcal": 364, "carb": 76.3, "sugar": 0.3, "protein": 11.8, "fat": 1.2, "sat_fat": 0.2, "trans_fat": 0, "cholesterol": 0, "sodium": 2},
    "프랑스밀가루":     {"kcal": 364, "carb": 76.3, "sugar": 0.3, "protein": 11.8, "fat": 1.2, "sat_fat": 0.2, "trans_fat": 0, "cholesterol": 0, "sodium": 2},
    "박력분":           {"kcal": 366, "carb": 77.7, "sugar": 0.3, "protein": 8.5, "fat": 1.5, "sat_fat": 0.2, "trans_fat": 0, "cholesterol": 0, "sodium": 2},
    "박력쌀가루":       {"kcal": 366, "carb": 80.1, "sugar": 0.5, "protein": 6.8, "fat": 0.7, "sat_fat": 0.2, "trans_fat": 0, "cholesterol": 0, "sodium": 5},
    "강력쌀가루":       {"kcal": 366, "carb": 80.1, "sugar": 0.5, "protein": 6.8, "fat": 0.7, "sat_fat": 0.2, "trans_fat": 0, "cholesterol": 0, "sodium": 5},
    "통밀가루":         {"kcal": 340, "carb": 72.0, "sugar": 0.4, "protein": 13.2, "fat": 2.5, "sat_fat": 0.4, "trans_fat": 0, "cholesterol": 0, "sodium": 2},
    "유기농통밀가루":   {"kcal": 340, "carb": 72.0, "sugar": 0.4, "protein": 13.2, "fat": 2.5, "sat_fat": 0.4, "trans_fat": 0, "cholesterol": 0, "sodium": 2},
    "호라산밀가루":     {"kcal": 337, "carb": 70.4, "sugar": 3.8, "protein": 14.5, "fat": 2.1, "sat_fat": 0.3, "trans_fat": 0, "cholesterol": 0, "sodium": 3},
    "호라산밀":         {"kcal": 337, "carb": 70.4, "sugar": 3.8, "protein": 14.5, "fat": 2.1, "sat_fat": 0.3, "trans_fat": 0, "cholesterol": 0, "sodium": 3},
    "찹쌀가루":         {"kcal": 370, "carb": 82.5, "sugar": 0.3, "protein": 6.3, "fat": 1.0, "sat_fat": 0.3, "trans_fat": 0, "cholesterol": 0, "sodium": 3},
    "타피오카전분":     {"kcal": 358, "carb": 88.7, "sugar": 0, "protein": 0.2, "fat": 0.0, "sat_fat": 0, "trans_fat": 0, "cholesterol": 0, "sodium": 1},
    "현미가루":         {"kcal": 363, "carb": 77.2, "sugar": 0.7, "protein": 7.9, "fat": 3.0, "sat_fat": 0.6, "trans_fat": 0, "cholesterol": 0, "sodium": 4},
    "발아현미가루":     {"kcal": 363, "carb": 77.2, "sugar": 0.7, "protein": 7.9, "fat": 3.0, "sat_fat": 0.6, "trans_fat": 0, "cholesterol": 0, "sodium": 4},
    "귀리가루":         {"kcal": 379, "carb": 67.7, "sugar": 1.0, "protein": 13.2, "fat": 6.5, "sat_fat": 1.1, "trans_fat": 0, "cholesterol": 0, "sodium": 2},
    "보리가루":         {"kcal": 345, "carb": 74.5, "sugar": 0.8, "protein": 10.5, "fat": 1.6, "sat_fat": 0.3, "trans_fat": 0, "cholesterol": 0, "sodium": 4},
    "옥수수전분":       {"kcal": 355, "carb": 87.6, "sugar": 0, "protein": 0.3, "fat": 0.1, "sat_fat": 0, "trans_fat": 0, "cholesterol": 0, "sodium": 2},
    "밀기울":           {"kcal": 216, "carb": 64.5, "sugar": 0.4, "protein": 15.5, "fat": 4.3, "sat_fat": 0.6, "trans_fat": 0, "cholesterol": 0, "sodium": 2},
    "리너지밀기울":     {"kcal": 216, "carb": 64.5, "sugar": 0.4, "protein": 15.5, "fat": 4.3, "sat_fat": 0.6, "trans_fat": 0, "cholesterol": 0, "sodium": 2},
    "BSG분말":          {"kcal": 200, "carb": 40.0, "sugar": 1.0, "protein": 20.0, "fat": 7.0, "sat_fat": 1.5, "trans_fat": 0, "cholesterol": 0, "sodium": 10},
    "전립분":           {"kcal": 340, "carb": 72.0, "sugar": 0.4, "protein": 13.2, "fat": 2.5, "sat_fat": 0.4, "trans_fat": 0, "cholesterol": 0, "sodium": 2},
    "홍국쌀가루":       {"kcal": 366, "carb": 80.1, "sugar": 0.5, "protein": 6.8, "fat": 0.7, "sat_fat": 0.2, "trans_fat": 0, "cholesterol": 0, "sodium": 5},
    "통밀식빵가루":     {"kcal": 340, "carb": 72.0, "sugar": 2.0, "protein": 13.0, "fat": 2.5, "sat_fat": 0.4, "trans_fat": 0, "cholesterol": 0, "sodium": 200},

    # ============================================================
    # 단백질 원료
    # ============================================================
    "대두단백질":       {"kcal": 335, "carb": 10.0, "sugar": 0, "protein": 80.0, "fat": 1.0, "sat_fat": 0.2, "trans_fat": 0, "cholesterol": 0, "sodium": 1100},
    "완두단백분말":     {"kcal": 370, "carb": 5.0, "sugar": 0, "protein": 80.0, "fat": 5.0, "sat_fat": 1.0, "trans_fat": 0, "cholesterol": 0, "sodium": 800},
    "병아리콩분말":     {"kcal": 364, "carb": 57.8, "sugar": 10.7, "protein": 22.4, "fat": 6.7, "sat_fat": 0.6, "trans_fat": 0, "cholesterol": 0, "sodium": 64},
    "칙피스":           {"kcal": 364, "carb": 57.8, "sugar": 10.7, "protein": 22.4, "fat": 6.7, "sat_fat": 0.6, "trans_fat": 0, "cholesterol": 0, "sodium": 64},
    "활성밀글루텐":     {"kcal": 370, "carb": 13.0, "sugar": 0.5, "protein": 75.0, "fat": 1.8, "sat_fat": 0.3, "trans_fat": 0, "cholesterol": 0, "sodium": 30},

    # ============================================================
    # 제빵 부재료/프리믹스
    # ============================================================
    "크라프트콘":       {"kcal": 355, "carb": 87.6, "sugar": 0, "protein": 0.3, "fat": 0.1, "sat_fat": 0, "trans_fat": 0, "cholesterol": 0, "sodium": 2},
    "베스트프리":       {"kcal": 350, "carb": 75.0, "sugar": 2.0, "protein": 12.0, "fat": 1.5, "sat_fat": 0.3, "trans_fat": 0, "cholesterol": 0, "sodium": 5},

    # ============================================================
    # 견과류/씨앗
    # ============================================================
    "아몬드분말":       {"kcal": 598, "carb": 19.3, "sugar": 4.0, "protein": 21.2, "fat": 52.5, "sat_fat": 4.0, "trans_fat": 0, "cholesterol": 0, "sodium": 1},
    "아몬드슬라이스":   {"kcal": 579, "carb": 21.6, "sugar": 4.4, "protein": 21.2, "fat": 49.9, "sat_fat": 3.8, "trans_fat": 0, "cholesterol": 0, "sodium": 1},
    "코코넛분말":       {"kcal": 660, "carb": 6.3, "sugar": 6.0, "protein": 6.9, "fat": 65.0, "sat_fat": 57.2, "trans_fat": 0, "cholesterol": 0, "sodium": 20},
    "흑임자분말":       {"kcal": 586, "carb": 17.0, "sugar": 0.5, "protein": 20.2, "fat": 51.6, "sat_fat": 7.2, "trans_fat": 0, "cholesterol": 0, "sodium": 5},
    "호두":             {"kcal": 654, "carb": 13.7, "sugar": 2.6, "protein": 15.2, "fat": 65.2, "sat_fat": 6.1, "trans_fat": 0, "cholesterol": 0, "sodium": 2},
    "호두분태":         {"kcal": 654, "carb": 13.7, "sugar": 2.6, "protein": 15.2, "fat": 65.2, "sat_fat": 6.1, "trans_fat": 0, "cholesterol": 0, "sodium": 2},
    "피칸":             {"kcal": 691, "carb": 13.9, "sugar": 4.0, "protein": 9.2, "fat": 72.0, "sat_fat": 6.2, "trans_fat": 0, "cholesterol": 0, "sodium": 0},
    "아몬드":           {"kcal": 579, "carb": 21.6, "sugar": 4.4, "protein": 21.2, "fat": 49.9, "sat_fat": 3.8, "trans_fat": 0, "cholesterol": 0, "sodium": 1},
    "피스타치오":       {"kcal": 560, "carb": 27.2, "sugar": 7.7, "protein": 20.2, "fat": 45.3, "sat_fat": 5.6, "trans_fat": 0, "cholesterol": 0, "sodium": 1},
    "피스타치오페이스트": {"kcal": 560, "carb": 27.2, "sugar": 7.7, "protein": 20.2, "fat": 45.3, "sat_fat": 5.6, "trans_fat": 0, "cholesterol": 0, "sodium": 1},
    "피스타치오분태":   {"kcal": 560, "carb": 27.2, "sugar": 7.7, "protein": 20.2, "fat": 45.3, "sat_fat": 5.6, "trans_fat": 0, "cholesterol": 0, "sodium": 1},
    "아마씨":           {"kcal": 534, "carb": 28.9, "sugar": 1.6, "protein": 18.3, "fat": 42.2, "sat_fat": 3.7, "trans_fat": 0, "cholesterol": 0, "sodium": 30},
    "해바라기씨":       {"kcal": 584, "carb": 20.0, "sugar": 2.6, "protein": 20.8, "fat": 51.5, "sat_fat": 4.5, "trans_fat": 0, "cholesterol": 0, "sodium": 9},
    "치아씨":           {"kcal": 486, "carb": 42.1, "sugar": 0, "protein": 16.5, "fat": 30.7, "sat_fat": 3.3, "trans_fat": 0, "cholesterol": 0, "sodium": 16},
    "참깨":             {"kcal": 565, "carb": 23.5, "sugar": 0.3, "protein": 17.0, "fat": 48.0, "sat_fat": 6.7, "trans_fat": 0, "cholesterol": 0, "sodium": 11},
    "호박씨":           {"kcal": 559, "carb": 10.7, "sugar": 1.4, "protein": 30.2, "fat": 49.1, "sat_fat": 8.7, "trans_fat": 0, "cholesterol": 0, "sodium": 7},
    "땅콩":             {"kcal": 567, "carb": 16.1, "sugar": 4.7, "protein": 25.8, "fat": 49.2, "sat_fat": 6.3, "trans_fat": 0, "cholesterol": 0, "sodium": 18},
    "땅콩버터":         {"kcal": 588, "carb": 20.0, "sugar": 9.2, "protein": 25.1, "fat": 50.4, "sat_fat": 10.3, "trans_fat": 0, "cholesterol": 0, "sodium": 426},
    "코코넛밀크":       {"kcal": 230, "carb": 5.5, "sugar": 3.3, "protein": 2.3, "fat": 23.8, "sat_fat": 21.1, "trans_fat": 0, "cholesterol": 0, "sodium": 15},

    # ============================================================
    # 건과일
    # ============================================================
    "크랜베리":         {"kcal": 308, "carb": 82.4, "sugar": 65.0, "protein": 0.1, "fat": 1.4, "sat_fat": 0.1, "trans_fat": 0, "cholesterol": 0, "sodium": 3},
    "건포도":           {"kcal": 296, "carb": 79.2, "sugar": 59.2, "protein": 3.1, "fat": 0.5, "sat_fat": 0.1, "trans_fat": 0, "cholesterol": 0, "sodium": 11},
    "바나나레즌":       {"kcal": 296, "carb": 79.2, "sugar": 59.2, "protein": 3.1, "fat": 0.5, "sat_fat": 0.1, "trans_fat": 0, "cholesterol": 0, "sodium": 11},
    "무화과":           {"kcal": 249, "carb": 63.9, "sugar": 47.9, "protein": 3.3, "fat": 0.9, "sat_fat": 0.1, "trans_fat": 0, "cholesterol": 0, "sodium": 10},
    "멜론레진":         {"kcal": 280, "carb": 72.0, "sugar": 55.0, "protein": 1.0, "fat": 0.3, "sat_fat": 0, "trans_fat": 0, "cholesterol": 0, "sodium": 10},

    # ============================================================
    # 감미료
    # ============================================================
    "하얀설탕":         {"kcal": 387, "carb": 99.8, "sugar": 99.8, "protein": 0, "fat": 0, "sat_fat": 0, "trans_fat": 0, "cholesterol": 0, "sodium": 0},
    "설탕":             {"kcal": 387, "carb": 99.8, "sugar": 99.8, "protein": 0, "fat": 0, "sat_fat": 0, "trans_fat": 0, "cholesterol": 0, "sodium": 0},
    "유기농설탕":       {"kcal": 387, "carb": 99.8, "sugar": 99.8, "protein": 0, "fat": 0, "sat_fat": 0, "trans_fat": 0, "cholesterol": 0, "sodium": 0},
    "슈가파우더":       {"kcal": 387, "carb": 99.8, "sugar": 99.8, "protein": 0, "fat": 0, "sat_fat": 0, "trans_fat": 0, "cholesterol": 0, "sodium": 0},
    "흑설탕":           {"kcal": 354, "carb": 91.5, "sugar": 89.7, "protein": 0.1, "fat": 0, "sat_fat": 0, "trans_fat": 0, "cholesterol": 0, "sodium": 28},
    "물엿":             {"kcal": 328, "carb": 82.0, "sugar": 20.0, "protein": 0, "fat": 0, "sat_fat": 0, "trans_fat": 0, "cholesterol": 0, "sodium": 18},
    "올리고당":         {"kcal": 280, "carb": 75.0, "sugar": 25.0, "protein": 0, "fat": 0, "sat_fat": 0, "trans_fat": 0, "cholesterol": 0, "sodium": 10},
    "꿀":               {"kcal": 302, "carb": 81.3, "sugar": 78.0, "protein": 0.3, "fat": 0, "sat_fat": 0, "trans_fat": 0, "cholesterol": 0, "sodium": 4},
    "스테비아":         {"kcal": 0, "carb": 0, "sugar": 0, "protein": 0, "fat": 0, "sat_fat": 0, "trans_fat": 0, "cholesterol": 0, "sodium": 0},
    "에리스리톨":       {"kcal": 0, "carb": 100.0, "sugar": 0, "protein": 0, "fat": 0, "sat_fat": 0, "trans_fat": 0, "cholesterol": 0, "sodium": 0},
    "알룰로오스":       {"kcal": 0, "carb": 100.0, "sugar": 0, "protein": 0, "fat": 0, "sat_fat": 0, "trans_fat": 0, "cholesterol": 0, "sodium": 0},
    "자일로스":         {"kcal": 0, "carb": 100.0, "sugar": 0, "protein": 0, "fat": 0, "sat_fat": 0, "trans_fat": 0, "cholesterol": 0, "sodium": 0},

    # ============================================================
    # 유지류
    # ============================================================
    "현미유":           {"kcal": 884, "carb": 0, "sugar": 0, "protein": 0, "fat": 100.0, "sat_fat": 20.0, "trans_fat": 0, "cholesterol": 0, "sodium": 0},
    "올리브유":         {"kcal": 884, "carb": 0, "sugar": 0, "protein": 0, "fat": 100.0, "sat_fat": 14.0, "trans_fat": 0, "cholesterol": 0, "sodium": 0},
    "코코넛오일":       {"kcal": 862, "carb": 0, "sugar": 0, "protein": 0, "fat": 100.0, "sat_fat": 82.5, "trans_fat": 0, "cholesterol": 0, "sodium": 0},
    "포도씨유":         {"kcal": 884, "carb": 0, "sugar": 0, "protein": 0, "fat": 100.0, "sat_fat": 10.0, "trans_fat": 0, "cholesterol": 0, "sodium": 0},
    "버터":             {"kcal": 717, "carb": 0.1, "sugar": 0.1, "protein": 0.9, "fat": 81.1, "sat_fat": 51.4, "trans_fat": 3.3, "cholesterol": 215, "sodium": 11},
    "무염버터":         {"kcal": 717, "carb": 0.1, "sugar": 0.1, "protein": 0.9, "fat": 81.1, "sat_fat": 51.4, "trans_fat": 3.3, "cholesterol": 215, "sodium": 11},
    "참기름":           {"kcal": 884, "carb": 0, "sugar": 0, "protein": 0, "fat": 100.0, "sat_fat": 14.2, "trans_fat": 0, "cholesterol": 0, "sodium": 0},
    "카놀라유":         {"kcal": 884, "carb": 0, "sugar": 0, "protein": 0, "fat": 100.0, "sat_fat": 7.4, "trans_fat": 0, "cholesterol": 0, "sodium": 0},
    "식용유":           {"kcal": 884, "carb": 0, "sugar": 0, "protein": 0, "fat": 100.0, "sat_fat": 15.0, "trans_fat": 0, "cholesterol": 0, "sodium": 0},
    "카카오버터":       {"kcal": 884, "carb": 0, "sugar": 0, "protein": 0, "fat": 100.0, "sat_fat": 60.0, "trans_fat": 0, "cholesterol": 0, "sodium": 0},
    "트러플오일":       {"kcal": 884, "carb": 0, "sugar": 0, "protein": 0, "fat": 100.0, "sat_fat": 14.0, "trans_fat": 0, "cholesterol": 0, "sodium": 0},

    # ============================================================
    # 비건 마가린/블록
    # ============================================================
    "유기농비건블록":   {"kcal": 747, "carb": 0, "sugar": 0, "protein": 0, "fat": 83.0, "sat_fat": 37.0, "trans_fat": 0, "cholesterol": 0, "sodium": 5},
    "유기농블락":       {"kcal": 747, "carb": 0, "sugar": 0, "protein": 0, "fat": 83.0, "sat_fat": 37.0, "trans_fat": 0, "cholesterol": 0, "sodium": 5},

    # ============================================================
    # 유제품/대체유
    # ============================================================
    "두유":             {"kcal": 42, "carb": 2.9, "sugar": 1.8, "protein": 3.5, "fat": 1.9, "sat_fat": 0.3, "trans_fat": 0, "cholesterol": 0, "sodium": 32},
    "우유":             {"kcal": 63, "carb": 4.7, "sugar": 4.7, "protein": 3.2, "fat": 3.5, "sat_fat": 2.2, "trans_fat": 0, "cholesterol": 11, "sodium": 40},
    "생크림":           {"kcal": 345, "carb": 2.8, "sugar": 2.8, "protein": 2.1, "fat": 36.1, "sat_fat": 22.5, "trans_fat": 1.0, "cholesterol": 137, "sodium": 38},
    "식물성크림":       {"kcal": 290, "carb": 18.0, "sugar": 5.0, "protein": 1.0, "fat": 24.0, "sat_fat": 22.0, "trans_fat": 0, "cholesterol": 0, "sodium": 50},
    "크림치즈":         {"kcal": 342, "carb": 4.1, "sugar": 3.2, "protein": 6.2, "fat": 34.0, "sat_fat": 19.2, "trans_fat": 0, "cholesterol": 110, "sodium": 321},
    "마스카포네치즈":   {"kcal": 429, "carb": 3.5, "sugar": 3.5, "protein": 4.8, "fat": 44.0, "sat_fat": 28.0, "trans_fat": 0, "cholesterol": 105, "sodium": 50},
    "연유":             {"kcal": 321, "carb": 54.4, "sugar": 54.4, "protein": 7.9, "fat": 8.7, "sat_fat": 5.5, "trans_fat": 0, "cholesterol": 34, "sodium": 128},
    "탈지분유":         {"kcal": 362, "carb": 51.0, "sugar": 51.0, "protein": 36.2, "fat": 0.8, "sat_fat": 0.5, "trans_fat": 0, "cholesterol": 18, "sodium": 535},
    "요거트":           {"kcal": 63, "carb": 7.0, "sugar": 7.0, "protein": 5.3, "fat": 1.6, "sat_fat": 1.0, "trans_fat": 0, "cholesterol": 6, "sodium": 70},
    "비건체다치즈향소스": {"kcal": 250, "carb": 10.0, "sugar": 2.0, "protein": 2.0, "fat": 22.0, "sat_fat": 15.0, "trans_fat": 0, "cholesterol": 0, "sodium": 800},
    "식물성마요네즈":   {"kcal": 680, "carb": 3.0, "sugar": 2.0, "protein": 1.0, "fat": 74.0, "sat_fat": 6.0, "trans_fat": 0, "cholesterol": 0, "sodium": 600},

    # ============================================================
    # 달걀
    # ============================================================
    "계란":             {"kcal": 147, "carb": 0.8, "sugar": 0.4, "protein": 12.6, "fat": 10.0, "sat_fat": 3.1, "trans_fat": 0, "cholesterol": 372, "sodium": 140},
    "전란":             {"kcal": 147, "carb": 0.8, "sugar": 0.4, "protein": 12.6, "fat": 10.0, "sat_fat": 3.1, "trans_fat": 0, "cholesterol": 372, "sodium": 140},
    "전란액":           {"kcal": 147, "carb": 0.8, "sugar": 0.4, "protein": 12.6, "fat": 10.0, "sat_fat": 3.1, "trans_fat": 0, "cholesterol": 372, "sodium": 140},
    "난황":             {"kcal": 352, "carb": 0.7, "sugar": 0.6, "protein": 16.0, "fat": 31.9, "sat_fat": 9.6, "trans_fat": 0, "cholesterol": 1085, "sodium": 48},
    "난백":             {"kcal": 47, "carb": 0.7, "sugar": 0.7, "protein": 10.9, "fat": 0.2, "sat_fat": 0, "trans_fat": 0, "cholesterol": 0, "sodium": 166},

    # ============================================================
    # 발효/팽창제
    # ============================================================
    "드라이이스트":     {"kcal": 325, "carb": 41.2, "sugar": 0, "protein": 40.4, "fat": 7.6, "sat_fat": 1.0, "trans_fat": 0, "cholesterol": 0, "sodium": 51},
    "생이스트":         {"kcal": 105, "carb": 18.1, "sugar": 0, "protein": 8.4, "fat": 1.9, "sat_fat": 0.2, "trans_fat": 0, "cholesterol": 0, "sodium": 16},
    "베이킹파우더":     {"kcal": 53, "carb": 27.7, "sugar": 0, "protein": 0, "fat": 0, "sat_fat": 0, "trans_fat": 0, "cholesterol": 0, "sodium": 10600},
    "베이킹소다":       {"kcal": 0, "carb": 0, "sugar": 0, "protein": 0, "fat": 0, "sat_fat": 0, "trans_fat": 0, "cholesterol": 0, "sodium": 27360},

    # ============================================================
    # 소금/조미료
    # ============================================================
    "정제소금":         {"kcal": 0, "carb": 0, "sugar": 0, "protein": 0, "fat": 0, "sat_fat": 0, "trans_fat": 0, "cholesterol": 0, "sodium": 38758},
    "천일염":           {"kcal": 0, "carb": 0, "sugar": 0, "protein": 0, "fat": 0, "sat_fat": 0, "trans_fat": 0, "cholesterol": 0, "sodium": 35000},
    "순후추":           {"kcal": 251, "carb": 63.9, "sugar": 0.6, "protein": 10.4, "fat": 3.3, "sat_fat": 1.4, "trans_fat": 0, "cholesterol": 0, "sodium": 20},
    "계피분말":         {"kcal": 247, "carb": 80.6, "sugar": 2.2, "protein": 4.0, "fat": 1.2, "sat_fat": 0.3, "trans_fat": 0, "cholesterol": 0, "sodium": 10},
    "바닐라에센스":     {"kcal": 288, "carb": 12.7, "sugar": 12.7, "protein": 0.1, "fat": 0.1, "sat_fat": 0, "trans_fat": 0, "cholesterol": 0, "sodium": 9},
    "바닐라빈":         {"kcal": 288, "carb": 12.7, "sugar": 12.7, "protein": 0.1, "fat": 0.1, "sat_fat": 0, "trans_fat": 0, "cholesterol": 0, "sodium": 9},
    "간장":             {"kcal": 53, "carb": 5.6, "sugar": 1.0, "protein": 8.1, "fat": 0, "sat_fat": 0, "trans_fat": 0, "cholesterol": 0, "sodium": 5637},
    "태양초고추장":     {"kcal": 170, "carb": 37.0, "sugar": 15.0, "protein": 5.0, "fat": 1.5, "sat_fat": 0.3, "trans_fat": 0, "cholesterol": 0, "sodium": 2100},

    # ============================================================
    # 초콜릿/카카오
    # ============================================================
    "코코아파우더":     {"kcal": 228, "carb": 57.9, "sugar": 1.8, "protein": 19.6, "fat": 13.7, "sat_fat": 8.1, "trans_fat": 0, "cholesterol": 0, "sodium": 21},
    "다크초콜릿":       {"kcal": 546, "carb": 59.4, "sugar": 48.0, "protein": 5.5, "fat": 31.3, "sat_fat": 18.5, "trans_fat": 0, "cholesterol": 2, "sodium": 7},
    "화이트초콜릿":     {"kcal": 539, "carb": 59.2, "sugar": 59.0, "protein": 5.9, "fat": 32.1, "sat_fat": 19.4, "trans_fat": 0, "cholesterol": 21, "sodium": 90},
    "초코칩":           {"kcal": 546, "carb": 59.4, "sugar": 48.0, "protein": 5.5, "fat": 31.3, "sat_fat": 18.5, "trans_fat": 0, "cholesterol": 2, "sodium": 7},
    "초코칩(동물성)":   {"kcal": 546, "carb": 59.4, "sugar": 48.0, "protein": 5.5, "fat": 31.3, "sat_fat": 18.5, "trans_fat": 0, "cholesterol": 2, "sodium": 7},
    "카카오닙스":       {"kcal": 460, "carb": 34.7, "sugar": 0, "protein": 12.4, "fat": 43.1, "sat_fat": 25.0, "trans_fat": 0, "cholesterol": 0, "sodium": 21},

    # ============================================================
    # 과일/채소
    # ============================================================
    "레몬즙":           {"kcal": 22, "carb": 6.9, "sugar": 2.5, "protein": 0.4, "fat": 0.2, "sat_fat": 0, "trans_fat": 0, "cholesterol": 0, "sodium": 1},
    "레몬제스트":       {"kcal": 47, "carb": 16.0, "sugar": 4.2, "protein": 1.5, "fat": 0.3, "sat_fat": 0, "trans_fat": 0, "cholesterol": 0, "sodium": 6},
    "바나나":           {"kcal": 89, "carb": 22.8, "sugar": 12.2, "protein": 1.1, "fat": 0.3, "sat_fat": 0.1, "trans_fat": 0, "cholesterol": 0, "sodium": 1},
    "양파":             {"kcal": 40, "carb": 9.3, "sugar": 4.2, "protein": 1.1, "fat": 0.1, "sat_fat": 0, "trans_fat": 0, "cholesterol": 0, "sodium": 4},
    "양파분태":         {"kcal": 350, "carb": 82.0, "sugar": 35.0, "protein": 9.0, "fat": 0.5, "sat_fat": 0, "trans_fat": 0, "cholesterol": 0, "sodium": 40},
    "호박":             {"kcal": 26, "carb": 6.5, "sugar": 2.8, "protein": 1.0, "fat": 0.1, "sat_fat": 0, "trans_fat": 0, "cholesterol": 0, "sodium": 1},
    "단호박":           {"kcal": 26, "carb": 6.5, "sugar": 2.8, "protein": 1.0, "fat": 0.1, "sat_fat": 0, "trans_fat": 0, "cholesterol": 0, "sodium": 1},
    "고구마":           {"kcal": 86, "carb": 20.1, "sugar": 4.2, "protein": 1.6, "fat": 0.1, "sat_fat": 0, "trans_fat": 0, "cholesterol": 0, "sodium": 55},
    "감자":             {"kcal": 77, "carb": 17.5, "sugar": 0.8, "protein": 2.0, "fat": 0.1, "sat_fat": 0, "trans_fat": 0, "cholesterol": 0, "sodium": 6},
    "대파":             {"kcal": 27, "carb": 5.7, "sugar": 2.3, "protein": 1.5, "fat": 0.3, "sat_fat": 0, "trans_fat": 0, "cholesterol": 0, "sodium": 5},
    "냉동대파":         {"kcal": 27, "carb": 5.7, "sugar": 2.3, "protein": 1.5, "fat": 0.3, "sat_fat": 0, "trans_fat": 0, "cholesterol": 0, "sodium": 5},
    "마늘":             {"kcal": 149, "carb": 33.1, "sugar": 1.0, "protein": 6.4, "fat": 0.5, "sat_fat": 0.1, "trans_fat": 0, "cholesterol": 0, "sodium": 17},
    "쑥":               {"kcal": 46, "carb": 8.6, "sugar": 0.5, "protein": 5.2, "fat": 0.7, "sat_fat": 0.1, "trans_fat": 0, "cholesterol": 0, "sodium": 60},
    "쑥분말":           {"kcal": 280, "carb": 50.0, "sugar": 3.0, "protein": 25.0, "fat": 4.0, "sat_fat": 0.5, "trans_fat": 0, "cholesterol": 0, "sodium": 50},
    "당근":             {"kcal": 41, "carb": 9.6, "sugar": 4.7, "protein": 0.9, "fat": 0.2, "sat_fat": 0, "trans_fat": 0, "cholesterol": 0, "sodium": 69},
    "파슬리":           {"kcal": 36, "carb": 6.3, "sugar": 0.9, "protein": 3.0, "fat": 0.8, "sat_fat": 0.1, "trans_fat": 0, "cholesterol": 0, "sodium": 56},
    "블랙올리브":       {"kcal": 115, "carb": 6.3, "sugar": 0, "protein": 0.8, "fat": 10.7, "sat_fat": 1.4, "trans_fat": 0, "cholesterol": 0, "sodium": 735},
    "새송이버섯":       {"kcal": 35, "carb": 6.1, "sugar": 1.9, "protein": 3.3, "fat": 0.4, "sat_fat": 0.1, "trans_fat": 0, "cholesterol": 0, "sodium": 18},
    "오이피클":         {"kcal": 11, "carb": 2.3, "sugar": 1.1, "protein": 0.3, "fat": 0.2, "sat_fat": 0, "trans_fat": 0, "cholesterol": 0, "sodium": 1208},

    # ============================================================
    # 콩류/앙금
    # ============================================================
    "팥":               {"kcal": 329, "carb": 56.7, "sugar": 1.3, "protein": 20.5, "fat": 1.2, "sat_fat": 0.2, "trans_fat": 0, "cholesterol": 0, "sodium": 3},
    "팥앙금":           {"kcal": 250, "carb": 55.0, "sugar": 35.0, "protein": 6.0, "fat": 0.5, "sat_fat": 0.1, "trans_fat": 0, "cholesterol": 0, "sodium": 5},
    "팥앙금(자체)":     {"kcal": 230, "carb": 50.0, "sugar": 20.0, "protein": 8.0, "fat": 0.5, "sat_fat": 0.1, "trans_fat": 0, "cholesterol": 0, "sodium": 3},
    "통팥앙금":         {"kcal": 250, "carb": 55.0, "sugar": 35.0, "protein": 6.0, "fat": 0.5, "sat_fat": 0.1, "trans_fat": 0, "cholesterol": 0, "sodium": 5},
    "두부":             {"kcal": 76, "carb": 1.9, "sugar": 0.6, "protein": 8.1, "fat": 4.2, "sat_fat": 0.6, "trans_fat": 0, "cholesterol": 0, "sodium": 7},

    # ============================================================
    # 제빵 개량제/부재료
    # ============================================================
    "엔지마띠코":       {"kcal": 350, "carb": 75.0, "sugar": 2.0, "protein": 12.0, "fat": 1.5, "sat_fat": 0.3, "trans_fat": 0, "cholesterol": 0, "sodium": 5},
    "에스피":           {"kcal": 350, "carb": 75.0, "sugar": 2.0, "protein": 12.0, "fat": 1.5, "sat_fat": 0.3, "trans_fat": 0, "cholesterol": 0, "sodium": 5},
    "엑셀런스":         {"kcal": 350, "carb": 75.0, "sugar": 2.0, "protein": 12.0, "fat": 1.5, "sat_fat": 0.3, "trans_fat": 0, "cholesterol": 0, "sodium": 5},
    "몰트액기스":       {"kcal": 320, "carb": 78.0, "sugar": 40.0, "protein": 2.0, "fat": 0, "sat_fat": 0, "trans_fat": 0, "cholesterol": 0, "sodium": 35},
    "맥아분말":         {"kcal": 361, "carb": 77.0, "sugar": 18.0, "protein": 10.3, "fat": 1.8, "sat_fat": 0.3, "trans_fat": 0, "cholesterol": 0, "sodium": 14},
    "데코젤미로와":     {"kcal": 250, "carb": 62.0, "sugar": 40.0, "protein": 0, "fat": 0, "sat_fat": 0, "trans_fat": 0, "cholesterol": 0, "sodium": 10},
    "홍국적색소":       {"kcal": 0, "carb": 0, "sugar": 0, "protein": 0, "fat": 0, "sat_fat": 0, "trans_fat": 0, "cholesterol": 0, "sodium": 0},
    "블루색소":         {"kcal": 0, "carb": 0, "sugar": 0, "protein": 0, "fat": 0, "sat_fat": 0, "trans_fat": 0, "cholesterol": 0, "sodium": 0},
    "민트그린색소":     {"kcal": 0, "carb": 0, "sugar": 0, "protein": 0, "fat": 0, "sat_fat": 0, "trans_fat": 0, "cholesterol": 0, "sodium": 0},
    "비타민미네랄":     {"kcal": 0, "carb": 0, "sugar": 0, "protein": 0, "fat": 0, "sat_fat": 0, "trans_fat": 0, "cholesterol": 0, "sodium": 0},

    # ============================================================
    # 물/주류
    # ============================================================
    "정제수":           {"kcal": 0, "carb": 0, "sugar": 0, "protein": 0, "fat": 0, "sat_fat": 0, "trans_fat": 0, "cholesterol": 0, "sodium": 0},
    "물":               {"kcal": 0, "carb": 0, "sugar": 0, "protein": 0, "fat": 0, "sat_fat": 0, "trans_fat": 0, "cholesterol": 0, "sodium": 0},
    "럼주":             {"kcal": 231, "carb": 0, "sugar": 0, "protein": 0, "fat": 0, "sat_fat": 0, "trans_fat": 0, "cholesterol": 0, "sodium": 1},
    "트리플섹":         {"kcal": 250, "carb": 27.0, "sugar": 27.0, "protein": 0, "fat": 0, "sat_fat": 0, "trans_fat": 0, "cholesterol": 0, "sodium": 0},
    "트리플색":         {"kcal": 250, "carb": 27.0, "sugar": 27.0, "protein": 0, "fat": 0, "sat_fat": 0, "trans_fat": 0, "cholesterol": 0, "sodium": 0},

    # ============================================================
    # 유화제/첨가물 (극소량 - 영양 기여 미미)
    # ============================================================
    "레시틴":           {"kcal": 0, "carb": 0, "sugar": 0, "protein": 0, "fat": 0, "sat_fat": 0, "trans_fat": 0, "cholesterol": 0, "sodium": 0},
    "대두레시틴":       {"kcal": 0, "carb": 0, "sugar": 0, "protein": 0, "fat": 0, "sat_fat": 0, "trans_fat": 0, "cholesterol": 0, "sodium": 0},
    "잔탄검":           {"kcal": 0, "carb": 0, "sugar": 0, "protein": 0, "fat": 0, "sat_fat": 0, "trans_fat": 0, "cholesterol": 0, "sodium": 0},
    "구아검":           {"kcal": 0, "carb": 0, "sugar": 0, "protein": 0, "fat": 0, "sat_fat": 0, "trans_fat": 0, "cholesterol": 0, "sodium": 0},
    "펙틴":             {"kcal": 0, "carb": 0, "sugar": 0, "protein": 0, "fat": 0, "sat_fat": 0, "trans_fat": 0, "cholesterol": 0, "sodium": 0},
    "젤라틴":           {"kcal": 335, "carb": 0, "sugar": 0, "protein": 85.6, "fat": 0.1, "sat_fat": 0, "trans_fat": 0, "cholesterol": 0, "sodium": 72},
    "한천":             {"kcal": 0, "carb": 0, "sugar": 0, "protein": 0, "fat": 0, "sat_fat": 0, "trans_fat": 0, "cholesterol": 0, "sodium": 9},
    "S.P":              {"kcal": 350, "carb": 75.0, "sugar": 2.0, "protein": 12.0, "fat": 1.5, "sat_fat": 0.3, "trans_fat": 0, "cholesterol": 0, "sodium": 5},

    # ============================================================
    # 기타 소스/토핑
    # ============================================================
    "로투스크럼블":     {"kcal": 480, "carb": 68.0, "sugar": 38.0, "protein": 3.5, "fat": 22.0, "sat_fat": 10.0, "trans_fat": 0, "cholesterol": 0, "sodium": 600},
    "라즈베리분말":     {"kcal": 280, "carb": 65.0, "sugar": 50.0, "protein": 5.0, "fat": 2.0, "sat_fat": 0.3, "trans_fat": 0, "cholesterol": 0, "sodium": 5},
    "코코아분말":       {"kcal": 228, "carb": 57.9, "sugar": 1.8, "protein": 19.6, "fat": 13.7, "sat_fat": 8.1, "trans_fat": 0, "cholesterol": 0, "sodium": 21},
    "토마토페이스트":   {"kcal": 82, "carb": 18.9, "sugar": 12.2, "protein": 4.3, "fat": 0.5, "sat_fat": 0.1, "trans_fat": 0, "cholesterol": 0, "sodium": 59},
    "아몬드슬라이스":   {"kcal": 579, "carb": 21.6, "sugar": 4.4, "protein": 21.2, "fat": 49.9, "sat_fat": 3.8, "trans_fat": 0, "cholesterol": 0, "sodium": 1},
    "트러플슬라이스":   {"kcal": 28, "carb": 5.0, "sugar": 0.5, "protein": 2.0, "fat": 0.5, "sat_fat": 0.1, "trans_fat": 0, "cholesterol": 0, "sodium": 5},

    # 참치/해산물
    "참치":             {"kcal": 132, "carb": 0, "sugar": 0, "protein": 28.0, "fat": 1.3, "sat_fat": 0.4, "trans_fat": 0, "cholesterol": 42, "sodium": 50},

    # 콩나물/채소
    "쌀눈유":           {"kcal": 884, "carb": 0, "sugar": 0, "protein": 0, "fat": 100.0, "sat_fat": 20.0, "trans_fat": 0, "cholesterol": 0, "sodium": 0},
}

NUTRIENT_KEYS = ["kcal", "carb", "sugar", "protein", "fat", "sat_fat", "trans_fat", "cholesterol", "sodium"]
NUTRIENT_LABELS = {
    "kcal": "열량(kcal)", "carb": "탄수화물(g)", "sugar": "당류(g)",
    "protein": "단백질(g)", "fat": "지방(g)", "sat_fat": "포화지방(g)",
    "trans_fat": "트랜스지방(g)", "cholesterol": "콜레스테롤(mg)", "sodium": "나트륨(mg)"
}

def get_nutrient(ingredient_name):
    """원재료명으로 영양성분 조회. 정규화 후 DB 검색."""
    norm = normalize_name(ingredient_name)
    return INGREDIENT_DB.get(norm, None)

def get_all_db_names():
    return set(INGREDIENT_DB.keys())
