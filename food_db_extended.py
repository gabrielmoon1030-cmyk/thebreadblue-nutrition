"""
확장 식품 영양성분 DB (식약처 식품성분표 기반)
- 농촌진흥청 국가표준식품성분표 + 식품안전나라 데이터 기반
- 베이커리 원재료 중심 500종+
- 100g당 기준
"""

# 가공식품/원재료 확장 DB
# 기본 DB(ingredient_db.py)에 없는 원재료를 여기서 보완
EXTENDED_DB = {
    # ============================================================
    # 밀가루/전분/곡물 추가
    # ============================================================
    "중력분": {"kcal": 364, "carb": 76.3, "sugar": 0.3, "protein": 10.0, "fat": 1.2, "sat_fat": 0.2, "trans_fat": 0, "cholesterol": 0, "sodium": 2},
    "강력분": {"kcal": 364, "carb": 72.5, "sugar": 0.3, "protein": 13.0, "fat": 1.5, "sat_fat": 0.2, "trans_fat": 0, "cholesterol": 0, "sodium": 2},
    "쌀가루": {"kcal": 366, "carb": 80.1, "sugar": 0.5, "protein": 6.8, "fat": 0.7, "sat_fat": 0.2, "trans_fat": 0, "cholesterol": 0, "sodium": 5},
    "감자전분": {"kcal": 333, "carb": 82.3, "sugar": 0, "protein": 0.1, "fat": 0.0, "sat_fat": 0, "trans_fat": 0, "cholesterol": 0, "sodium": 9},
    "메밀가루": {"kcal": 343, "carb": 71.5, "sugar": 2.6, "protein": 13.3, "fat": 3.4, "sat_fat": 0.7, "trans_fat": 0, "cholesterol": 0, "sodium": 1},
    "수수가루": {"kcal": 329, "carb": 72.1, "sugar": 1.5, "protein": 10.6, "fat": 3.5, "sat_fat": 0.6, "trans_fat": 0, "cholesterol": 0, "sodium": 2},
    "기장가루": {"kcal": 378, "carb": 72.8, "sugar": 1.3, "protein": 11.0, "fat": 4.2, "sat_fat": 0.7, "trans_fat": 0, "cholesterol": 0, "sodium": 5},
    "흑미가루": {"kcal": 356, "carb": 76.0, "sugar": 0.5, "protein": 8.3, "fat": 2.8, "sat_fat": 0.5, "trans_fat": 0, "cholesterol": 0, "sodium": 3},
    "율무가루": {"kcal": 370, "carb": 72.0, "sugar": 0.5, "protein": 13.0, "fat": 4.5, "sat_fat": 0.8, "trans_fat": 0, "cholesterol": 0, "sodium": 3},
    "퀴노아": {"kcal": 368, "carb": 64.2, "sugar": 2.0, "protein": 14.1, "fat": 6.1, "sat_fat": 0.7, "trans_fat": 0, "cholesterol": 0, "sodium": 5},
    "렌틸콩": {"kcal": 352, "carb": 60.1, "sugar": 2.0, "protein": 24.6, "fat": 1.1, "sat_fat": 0.2, "trans_fat": 0, "cholesterol": 0, "sodium": 6},
    "자색고구마분말": {"kcal": 340, "carb": 80.0, "sugar": 15.0, "protein": 3.0, "fat": 0.5, "sat_fat": 0.1, "trans_fat": 0, "cholesterol": 0, "sodium": 50},

    # ============================================================
    # 유제품/크림 추가
    # ============================================================
    "쿠킹크림": {"kcal": 195, "carb": 4.0, "sugar": 3.5, "protein": 2.5, "fat": 19.0, "sat_fat": 12.0, "trans_fat": 0.3, "cholesterol": 55, "sodium": 40},
    "사워크림": {"kcal": 198, "carb": 4.6, "sugar": 3.4, "protein": 2.4, "fat": 19.4, "sat_fat": 11.5, "trans_fat": 0, "cholesterol": 51, "sodium": 36},
    "버터밀크": {"kcal": 40, "carb": 4.8, "sugar": 4.8, "protein": 3.3, "fat": 0.9, "sat_fat": 0.5, "trans_fat": 0, "cholesterol": 4, "sodium": 105},
    "가염버터": {"kcal": 717, "carb": 0.1, "sugar": 0.1, "protein": 0.9, "fat": 81.1, "sat_fat": 51.4, "trans_fat": 3.3, "cholesterol": 215, "sodium": 643},
    "발효버터": {"kcal": 717, "carb": 0.1, "sugar": 0.1, "protein": 0.9, "fat": 81.1, "sat_fat": 51.4, "trans_fat": 3.3, "cholesterol": 215, "sodium": 11},
    "모짜렐라치즈": {"kcal": 280, "carb": 2.2, "sugar": 1.0, "protein": 28.0, "fat": 17.0, "sat_fat": 11.0, "trans_fat": 0, "cholesterol": 54, "sodium": 627},
    "파마산치즈": {"kcal": 431, "carb": 3.2, "sugar": 0.8, "protein": 38.5, "fat": 29.0, "sat_fat": 18.5, "trans_fat": 0, "cholesterol": 68, "sodium": 1529},
    "체다치즈": {"kcal": 403, "carb": 1.3, "sugar": 0.5, "protein": 24.9, "fat": 33.1, "sat_fat": 21.1, "trans_fat": 0, "cholesterol": 105, "sodium": 621},
    "고다치즈": {"kcal": 356, "carb": 2.2, "sugar": 0.6, "protein": 24.9, "fat": 27.4, "sat_fat": 17.6, "trans_fat": 0, "cholesterol": 114, "sodium": 819},
    "코코넛크림": {"kcal": 330, "carb": 6.6, "sugar": 3.3, "protein": 3.6, "fat": 33.5, "sat_fat": 29.7, "trans_fat": 0, "cholesterol": 0, "sodium": 4},
    "두유크림": {"kcal": 100, "carb": 8.0, "sugar": 3.0, "protein": 3.0, "fat": 6.0, "sat_fat": 1.0, "trans_fat": 0, "cholesterol": 0, "sodium": 30},
    "오트밀크": {"kcal": 48, "carb": 7.0, "sugar": 4.0, "protein": 1.0, "fat": 1.5, "sat_fat": 0.2, "trans_fat": 0, "cholesterol": 0, "sodium": 45},
    "아몬드밀크": {"kcal": 17, "carb": 0.6, "sugar": 0.3, "protein": 0.6, "fat": 1.1, "sat_fat": 0.1, "trans_fat": 0, "cholesterol": 0, "sodium": 67},

    # ============================================================
    # 초콜릿/카카오 추가
    # ============================================================
    "밀크초콜릿": {"kcal": 535, "carb": 59.4, "sugar": 52.0, "protein": 7.6, "fat": 29.7, "sat_fat": 18.5, "trans_fat": 0, "cholesterol": 23, "sodium": 79},
    "루비초콜릿": {"kcal": 545, "carb": 52.0, "sugar": 48.0, "protein": 6.5, "fat": 35.0, "sat_fat": 21.0, "trans_fat": 0, "cholesterol": 15, "sodium": 45},
    "코팅초콜릿": {"kcal": 546, "carb": 59.4, "sugar": 48.0, "protein": 5.5, "fat": 31.3, "sat_fat": 18.5, "trans_fat": 0, "cholesterol": 2, "sodium": 7},
    "컴파운드초콜릿": {"kcal": 530, "carb": 58.0, "sugar": 50.0, "protein": 5.0, "fat": 31.0, "sat_fat": 25.0, "trans_fat": 0, "cholesterol": 0, "sodium": 20},
    "다크컴파운드칩": {"kcal": 530, "carb": 58.0, "sugar": 50.0, "protein": 5.0, "fat": 31.0, "sat_fat": 25.0, "trans_fat": 0, "cholesterol": 0, "sodium": 20},
    "가나슈": {"kcal": 445, "carb": 40.0, "sugar": 35.0, "protein": 4.5, "fat": 30.0, "sat_fat": 18.0, "trans_fat": 0, "cholesterol": 40, "sodium": 30},
    "누텔라": {"kcal": 539, "carb": 57.5, "sugar": 56.3, "protein": 6.3, "fat": 30.9, "sat_fat": 10.6, "trans_fat": 0, "cholesterol": 0, "sodium": 41},

    # ============================================================
    # 견과/씨앗/건과 추가
    # ============================================================
    "캐슈넛": {"kcal": 553, "carb": 30.2, "sugar": 5.9, "protein": 18.2, "fat": 43.9, "sat_fat": 7.8, "trans_fat": 0, "cholesterol": 0, "sodium": 12},
    "마카다미아": {"kcal": 718, "carb": 13.8, "sugar": 4.6, "protein": 7.9, "fat": 75.8, "sat_fat": 12.1, "trans_fat": 0, "cholesterol": 0, "sodium": 5},
    "헤이즐넛": {"kcal": 628, "carb": 16.7, "sugar": 4.3, "protein": 15.0, "fat": 60.8, "sat_fat": 4.5, "trans_fat": 0, "cholesterol": 0, "sodium": 0},
    "코코넛슈레드": {"kcal": 660, "carb": 6.3, "sugar": 6.0, "protein": 6.9, "fat": 65.0, "sat_fat": 57.2, "trans_fat": 0, "cholesterol": 0, "sodium": 20},
    "코코넛플레이크": {"kcal": 660, "carb": 6.3, "sugar": 6.0, "protein": 6.9, "fat": 65.0, "sat_fat": 57.2, "trans_fat": 0, "cholesterol": 0, "sodium": 20},
    "대추야자": {"kcal": 277, "carb": 75.0, "sugar": 63.4, "protein": 1.8, "fat": 0.2, "sat_fat": 0, "trans_fat": 0, "cholesterol": 0, "sodium": 1},
    "건살구": {"kcal": 241, "carb": 62.6, "sugar": 53.4, "protein": 3.4, "fat": 0.5, "sat_fat": 0, "trans_fat": 0, "cholesterol": 0, "sodium": 10},
    "건블루베리": {"kcal": 317, "carb": 80.0, "sugar": 68.0, "protein": 2.5, "fat": 1.0, "sat_fat": 0.1, "trans_fat": 0, "cholesterol": 0, "sodium": 5},
    "건체리": {"kcal": 325, "carb": 78.0, "sugar": 67.0, "protein": 3.0, "fat": 1.1, "sat_fat": 0.2, "trans_fat": 0, "cholesterol": 0, "sodium": 3},
    "건망고": {"kcal": 319, "carb": 78.6, "sugar": 73.0, "protein": 2.4, "fat": 1.2, "sat_fat": 0.3, "trans_fat": 0, "cholesterol": 0, "sodium": 162},
    "귤피": {"kcal": 97, "carb": 25.0, "sugar": 10.0, "protein": 1.5, "fat": 0.3, "sat_fat": 0, "trans_fat": 0, "cholesterol": 0, "sodium": 2},
    "유자청": {"kcal": 262, "carb": 65.0, "sugar": 60.0, "protein": 0.5, "fat": 0.2, "sat_fat": 0, "trans_fat": 0, "cholesterol": 0, "sodium": 5},

    # ============================================================
    # 과일/채소/퓨레 추가
    # ============================================================
    "딸기": {"kcal": 32, "carb": 7.7, "sugar": 4.9, "protein": 0.7, "fat": 0.3, "sat_fat": 0, "trans_fat": 0, "cholesterol": 0, "sodium": 1},
    "블루베리": {"kcal": 57, "carb": 14.5, "sugar": 10.0, "protein": 0.7, "fat": 0.3, "sat_fat": 0, "trans_fat": 0, "cholesterol": 0, "sodium": 1},
    "라즈베리": {"kcal": 52, "carb": 11.9, "sugar": 4.4, "protein": 1.2, "fat": 0.7, "sat_fat": 0, "trans_fat": 0, "cholesterol": 0, "sodium": 1},
    "망고": {"kcal": 60, "carb": 15.0, "sugar": 13.7, "protein": 0.8, "fat": 0.4, "sat_fat": 0.1, "trans_fat": 0, "cholesterol": 0, "sodium": 1},
    "복숭아": {"kcal": 39, "carb": 9.5, "sugar": 8.4, "protein": 0.9, "fat": 0.3, "sat_fat": 0, "trans_fat": 0, "cholesterol": 0, "sodium": 0},
    "체리": {"kcal": 63, "carb": 16.0, "sugar": 12.8, "protein": 1.1, "fat": 0.2, "sat_fat": 0, "trans_fat": 0, "cholesterol": 0, "sodium": 0},
    "배": {"kcal": 57, "carb": 15.2, "sugar": 9.8, "protein": 0.4, "fat": 0.1, "sat_fat": 0, "trans_fat": 0, "cholesterol": 0, "sodium": 1},
    "사과퓨레": {"kcal": 68, "carb": 17.0, "sugar": 12.0, "protein": 0.3, "fat": 0.1, "sat_fat": 0, "trans_fat": 0, "cholesterol": 0, "sodium": 3},
    "호박퓨레": {"kcal": 34, "carb": 8.5, "sugar": 3.5, "protein": 1.1, "fat": 0.1, "sat_fat": 0, "trans_fat": 0, "cholesterol": 0, "sodium": 3},
    "고구마퓨레": {"kcal": 90, "carb": 21.0, "sugar": 6.5, "protein": 1.6, "fat": 0.1, "sat_fat": 0, "trans_fat": 0, "cholesterol": 0, "sodium": 36},
    "레몬커드": {"kcal": 280, "carb": 38.0, "sugar": 35.0, "protein": 2.5, "fat": 14.0, "sat_fat": 8.0, "trans_fat": 0, "cholesterol": 120, "sodium": 55},
    "잼": {"kcal": 250, "carb": 62.0, "sugar": 60.0, "protein": 0.5, "fat": 0.1, "sat_fat": 0, "trans_fat": 0, "cholesterol": 0, "sodium": 15},
    "딸기잼": {"kcal": 250, "carb": 62.0, "sugar": 60.0, "protein": 0.5, "fat": 0.1, "sat_fat": 0, "trans_fat": 0, "cholesterol": 0, "sodium": 15},
    "시금치": {"kcal": 23, "carb": 3.6, "sugar": 0.4, "protein": 2.9, "fat": 0.4, "sat_fat": 0.1, "trans_fat": 0, "cholesterol": 0, "sodium": 79},
    "브로콜리": {"kcal": 34, "carb": 6.6, "sugar": 1.7, "protein": 2.8, "fat": 0.4, "sat_fat": 0.1, "trans_fat": 0, "cholesterol": 0, "sodium": 33},
    "옥수수": {"kcal": 86, "carb": 19.0, "sugar": 3.2, "protein": 3.3, "fat": 1.4, "sat_fat": 0.2, "trans_fat": 0, "cholesterol": 0, "sodium": 15},
    "피망": {"kcal": 20, "carb": 4.6, "sugar": 2.4, "protein": 0.9, "fat": 0.2, "sat_fat": 0, "trans_fat": 0, "cholesterol": 0, "sodium": 3},
    "방울토마토": {"kcal": 18, "carb": 3.9, "sugar": 2.6, "protein": 0.9, "fat": 0.2, "sat_fat": 0, "trans_fat": 0, "cholesterol": 0, "sodium": 5},

    # ============================================================
    # 육류/해산물
    # ============================================================
    "베이컨": {"kcal": 417, "carb": 0, "sugar": 0, "protein": 13.7, "fat": 40.3, "sat_fat": 13.0, "trans_fat": 0, "cholesterol": 66, "sodium": 1717},
    "햄": {"kcal": 145, "carb": 1.5, "sugar": 1.0, "protein": 18.0, "fat": 7.0, "sat_fat": 2.5, "trans_fat": 0, "cholesterol": 55, "sodium": 1203},
    "소시지": {"kcal": 301, "carb": 2.0, "sugar": 1.0, "protein": 12.0, "fat": 27.0, "sat_fat": 10.0, "trans_fat": 0, "cholesterol": 72, "sodium": 1068},
    "참치캔": {"kcal": 198, "carb": 0, "sugar": 0, "protein": 29.1, "fat": 8.2, "sat_fat": 1.5, "trans_fat": 0, "cholesterol": 55, "sodium": 354},
    "새우": {"kcal": 99, "carb": 0.2, "sugar": 0, "protein": 20.1, "fat": 1.7, "sat_fat": 0.3, "trans_fat": 0, "cholesterol": 152, "sodium": 111},
    "게맛살": {"kcal": 95, "carb": 9.5, "sugar": 3.5, "protein": 8.5, "fat": 2.2, "sat_fat": 0.3, "trans_fat": 0, "cholesterol": 17, "sodium": 841},

    # ============================================================
    # 향료/차/음료
    # ============================================================
    "얼그레이티": {"kcal": 0, "carb": 0, "sugar": 0, "protein": 0, "fat": 0, "sat_fat": 0, "trans_fat": 0, "cholesterol": 0, "sodium": 0},
    "말차분말": {"kcal": 338, "carb": 38.5, "sugar": 0, "protein": 29.6, "fat": 5.3, "sat_fat": 1.0, "trans_fat": 0, "cholesterol": 0, "sodium": 6},
    "녹차분말": {"kcal": 338, "carb": 38.5, "sugar": 0, "protein": 29.6, "fat": 5.3, "sat_fat": 1.0, "trans_fat": 0, "cholesterol": 0, "sodium": 6},
    "커피분말": {"kcal": 353, "carb": 65.0, "sugar": 0, "protein": 12.6, "fat": 0.5, "sat_fat": 0, "trans_fat": 0, "cholesterol": 0, "sodium": 3},
    "에스프레소": {"kcal": 2, "carb": 0, "sugar": 0, "protein": 0.1, "fat": 0, "sat_fat": 0, "trans_fat": 0, "cholesterol": 0, "sodium": 5},
    "인스턴트커피": {"kcal": 353, "carb": 65.0, "sugar": 0, "protein": 12.6, "fat": 0.5, "sat_fat": 0, "trans_fat": 0, "cholesterol": 0, "sodium": 3},
    "로즈마리": {"kcal": 131, "carb": 20.7, "sugar": 0, "protein": 3.3, "fat": 5.9, "sat_fat": 2.8, "trans_fat": 0, "cholesterol": 0, "sodium": 26},
    "바질": {"kcal": 23, "carb": 2.7, "sugar": 0.3, "protein": 3.2, "fat": 0.6, "sat_fat": 0.1, "trans_fat": 0, "cholesterol": 0, "sodium": 4},
    "타임": {"kcal": 101, "carb": 24.5, "sugar": 0, "protein": 5.6, "fat": 1.7, "sat_fat": 0.5, "trans_fat": 0, "cholesterol": 0, "sodium": 9},
    "오레가노": {"kcal": 265, "carb": 68.9, "sugar": 4.1, "protein": 9.0, "fat": 4.3, "sat_fat": 1.6, "trans_fat": 0, "cholesterol": 0, "sodium": 25},

    # ============================================================
    # 제빵 부재료 추가
    # ============================================================
    "마지팬": {"kcal": 458, "carb": 49.0, "sugar": 44.0, "protein": 9.0, "fat": 25.0, "sat_fat": 2.0, "trans_fat": 0, "cholesterol": 0, "sodium": 8},
    "프랄리네": {"kcal": 580, "carb": 40.0, "sugar": 38.0, "protein": 12.0, "fat": 42.0, "sat_fat": 3.0, "trans_fat": 0, "cholesterol": 0, "sodium": 5},
    "크루아상생지": {"kcal": 406, "carb": 45.0, "sugar": 8.0, "protein": 8.5, "fat": 21.0, "sat_fat": 13.0, "trans_fat": 1.0, "cholesterol": 67, "sodium": 400},
    "파이생지": {"kcal": 400, "carb": 38.0, "sugar": 2.0, "protein": 5.0, "fat": 26.0, "sat_fat": 12.0, "trans_fat": 0.5, "cholesterol": 30, "sodium": 250},
    "슈크림": {"kcal": 250, "carb": 30.0, "sugar": 18.0, "protein": 5.0, "fat": 12.0, "sat_fat": 7.0, "trans_fat": 0, "cholesterol": 120, "sodium": 100},
    "커스터드크림": {"kcal": 180, "carb": 25.0, "sugar": 18.0, "protein": 4.0, "fat": 7.0, "sat_fat": 4.0, "trans_fat": 0, "cholesterol": 90, "sodium": 80},
    "커스터드파우더": {"kcal": 355, "carb": 88.0, "sugar": 0, "protein": 0.3, "fat": 0.1, "sat_fat": 0, "trans_fat": 0, "cholesterol": 0, "sodium": 2},
    "프로틴파우더": {"kcal": 380, "carb": 8.0, "sugar": 2.0, "protein": 75.0, "fat": 5.0, "sat_fat": 2.0, "trans_fat": 0, "cholesterol": 50, "sodium": 200},
    "활성밀글루텐": {"kcal": 370, "carb": 13.0, "sugar": 0.5, "protein": 75.0, "fat": 1.8, "sat_fat": 0.3, "trans_fat": 0, "cholesterol": 0, "sodium": 30},
    "크라프트브레드": {"kcal": 355, "carb": 87.6, "sugar": 0, "protein": 0.3, "fat": 0.1, "sat_fat": 0, "trans_fat": 0, "cholesterol": 0, "sodium": 2},

    # ============================================================
    # 소스/시럽
    # ============================================================
    "메이플시럽": {"kcal": 260, "carb": 67.0, "sugar": 60.5, "protein": 0, "fat": 0.1, "sat_fat": 0, "trans_fat": 0, "cholesterol": 0, "sodium": 12},
    "아가베시럽": {"kcal": 310, "carb": 76.0, "sugar": 68.0, "protein": 0.1, "fat": 0.5, "sat_fat": 0, "trans_fat": 0, "cholesterol": 0, "sodium": 4},
    "카라멜소스": {"kcal": 325, "carb": 65.0, "sugar": 55.0, "protein": 1.0, "fat": 7.0, "sat_fat": 4.5, "trans_fat": 0, "cholesterol": 15, "sodium": 220},
    "초콜릿소스": {"kcal": 330, "carb": 58.0, "sugar": 50.0, "protein": 3.0, "fat": 10.0, "sat_fat": 6.0, "trans_fat": 0, "cholesterol": 5, "sodium": 40},
    "연유소스": {"kcal": 321, "carb": 54.4, "sugar": 54.4, "protein": 7.9, "fat": 8.7, "sat_fat": 5.5, "trans_fat": 0, "cholesterol": 34, "sodium": 128},
    "크림치즈프로스팅": {"kcal": 350, "carb": 40.0, "sugar": 38.0, "protein": 3.0, "fat": 20.0, "sat_fat": 12.0, "trans_fat": 0, "cholesterol": 60, "sodium": 200},
    "케찹": {"kcal": 112, "carb": 25.8, "sugar": 22.8, "protein": 1.7, "fat": 0.1, "sat_fat": 0, "trans_fat": 0, "cholesterol": 0, "sodium": 907},
    "머스터드": {"kcal": 66, "carb": 5.8, "sugar": 3.0, "protein": 4.4, "fat": 3.3, "sat_fat": 0.2, "trans_fat": 0, "cholesterol": 0, "sodium": 1135},
    "마요네즈": {"kcal": 680, "carb": 1.0, "sugar": 0.7, "protein": 1.0, "fat": 74.9, "sat_fat": 5.8, "trans_fat": 0, "cholesterol": 42, "sodium": 635},
    "페스토": {"kcal": 320, "carb": 5.0, "sugar": 1.5, "protein": 5.5, "fat": 31.0, "sat_fat": 5.5, "trans_fat": 0, "cholesterol": 8, "sodium": 530},

    # ============================================================
    # 식이섬유/건강기능 원료
    # ============================================================
    "이눌린": {"kcal": 150, "carb": 100.0, "sugar": 0, "protein": 0, "fat": 0, "sat_fat": 0, "trans_fat": 0, "cholesterol": 0, "sodium": 0},
    "사일리움허스크": {"kcal": 200, "carb": 80.0, "sugar": 0, "protein": 5.0, "fat": 1.0, "sat_fat": 0, "trans_fat": 0, "cholesterol": 0, "sodium": 30},
    "콜라겐": {"kcal": 350, "carb": 0, "sugar": 0, "protein": 90.0, "fat": 0, "sat_fat": 0, "trans_fat": 0, "cholesterol": 0, "sodium": 50},
    "귀리식이섬유": {"kcal": 250, "carb": 70.0, "sugar": 0, "protein": 10.0, "fat": 3.0, "sat_fat": 0.5, "trans_fat": 0, "cholesterol": 0, "sodium": 5},
}
