import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

def crawl_naver_news_titles(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print("Failed to retrieve the webpage.")
        return []
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 네이버 검색결과에서 뉴스 제목을 가져오는 CSS 선택자
    news_titles = []
    for title in soup.select("a.news_tit"):
        news_titles.append(title.get_text())
    
    return news_titles

def save_to_excel(titles, filename="results.xlsx"):
    wb = Workbook()
    ws = wb.active
    ws.title = "News Titles"
    
    ws.append(["News Title"])
    
    for title in titles:
        ws.append([title])
    
    wb.save(filename)
    print(f"Results saved to {filename}")

if __name__ == "__main__":
    url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%B0%98%EB%8F%84%EC%B2%B4"
    titles = crawl_naver_news_titles(url)
    
    if titles:
        save_to_excel(titles)
    else:
        print("No news titles found.")
