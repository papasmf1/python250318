import openpyxl
from openpyxl import Workbook
import random

# 랜덤 데이터 생성을 위한 샘플 데이터 정의
제품유형 = ["스마트폰", "노트북", "태블릿", "스마트워치", "이어폰", "TV", "냉장고", "세탁기", "청소기", "에어컨"]
브랜드 = ["삼성", "LG", "애플", "소니", "파나소닉", "샤오미", "다이슨", "필립스", "보쉬", "일렉트로룩스"]

# 엑셀 워크북 생성
wb = Workbook()
ws = wb.active
ws.title = "전자제품 판매 데이터"

# 헤더 추가
ws.append(["제품ID", "제품명", "수량", "가격"])

# 100개의 데이터 생성 및 추가
for i in range(1, 101):
    #f-string을 사용하면 바로 변수명:포맷스트링 
    제품ID = f"PROD{i:03d}"
    유형 = random.choice(제품유형)
    브랜드명 = random.choice(브랜드)
    제품명 = f"{브랜드명} {유형} {random.randint(1, 10)}세대"
    수량 = random.randint(1, 50)
    
    # 제품 유형에 따라 가격대 다르게 설정
    if 유형 == "스마트폰" or 유형 == "노트북":
        가격 = random.randint(800000, 2500000)
    elif 유형 == "TV" or 유형 == "냉장고":
        가격 = random.randint(500000, 1800000)
    elif 유형 == "태블릿":
        가격 = random.randint(300000, 1200000)
    elif 유형 == "세탁기" or 유형 == "에어컨":
        가격 = random.randint(400000, 1000000)
    else:
        가격 = random.randint(50000, 500000)
    
    ws.append([제품ID, 제품명, 수량, 가격])

# 열 너비 자동 조정
for col in ws.columns:
    max_length = 0
    column = col[0].column_letter
    for cell in col:
        if cell.value:
            max_length = max(max_length, len(str(cell.value)))
    adjusted_width = (max_length + 2)
    ws.column_dimensions[column].width = adjusted_width

# 파일 저장
wb.save("products.xlsx")
print("products.xlsx 파일이 성공적으로 생성되었습니다.")