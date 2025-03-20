import requests
from bs4 import BeautifulSoup
import openpyxl
from datetime import datetime

# 네이버 검색 URL
url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%B0%98%EB%8F%84%EC%B2%B4"

# User-Agent 설정
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
}

# 웹 페이지 요청
response = requests.get(url, headers=headers)
response.raise_for_status()  # 요청이 성공했는지 확인

# BeautifulSoup 객체 생성
soup = BeautifulSoup(response.text, "html.parser")

# 뉴스 기사 제목 추출
# 네이버 검색 결과에서 뉴스 기사 제목은 여러 클래스에 분산되어 있을 수 있음
news_titles = []

# 뉴스 캐스트 섹션
news_cast_titles = soup.select("a.news_tit")
for title in news_cast_titles:
    news_titles.append(title.get_text().strip())

# 뉴스 스탠드 섹션
news_stand_titles = soup.select("div.news_area a.news_tit")
for title in news_stand_titles:
    news_titles.append(title.get_text().strip())

# 뉴스 클러스터 섹션
news_cluster_titles = soup.select("div.news_contents a.news_tit")
for title in news_cluster_titles:
    news_titles.append(title.get_text().strip())

# 중복 제거
news_titles = list(dict.fromkeys(news_titles))

print(f"총 {len(news_titles)}개의 뉴스 제목을 찾았습니다.")

# Excel 파일 생성 및 저장
workbook = openpyxl.Workbook()
sheet = workbook.active
sheet.title = "반도체 뉴스"

# 헤더 추가
sheet["A1"] = "번호"
sheet["B1"] = "뉴스 제목"
sheet["C1"] = "수집 날짜"

# 데이터 추가
current_date = datetime.now().strftime("%Y-%m-%d")
for idx, title in enumerate(news_titles, 1):
    sheet[f"A{idx+1}"] = idx
    sheet[f"B{idx+1}"] = title
    sheet[f"C{idx+1}"] = current_date

# 열 너비 조정
sheet.column_dimensions["A"].width = 6
sheet.column_dimensions["B"].width = 70
sheet.column_dimensions["C"].width = 15

# 파일 저장
excel_path = "c:\\work\\results.xlsx"
workbook.save(excel_path)

print(f"뉴스 제목이 {excel_path}에 저장되었습니다.")