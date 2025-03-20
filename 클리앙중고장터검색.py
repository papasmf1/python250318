# coding:utf-8
#웹크롤링 
from bs4 import BeautifulSoup
#웹서버에 요청 
import urllib.request
#특정 문자열 검색 
import re 

#User-Agent를 조작하는 경우(아이폰에서 사용하는 사파리 브라우져의 헤더) 
hdr = {'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1'}

#파일에 쓰기
f = open("c:\\work\\clien.txt", "wt", encoding="utf-8")
#페이징하는 URL주소를 조립 
for n in range(0,10):
        #클리앙의 중고장터 주소 
        data ='https://www.clien.net/service/board/sold?&od=T31&po=' + str(n)
        print(data)
        #웹브라우져 헤더 추가 
        req = urllib.request.Request(data, \
                                    headers = hdr)
        data = urllib.request.urlopen(req).read()
        page = data.decode('utf-8', 'ignore')
        soup = BeautifulSoup(page, 'html.parser')
        list = soup.find_all('span', attrs={'data-role':'list-title-text'})
        # <span class="subject_fixed" data-role="list-title-text" title="플레이스테이션5 (PS5) 슬림 디지털 에디션 팝니다. (택포 40만원)">
	# 	플레이스테이션5 (PS5) 슬림 디지털 에디션 팝니다. (택포 40만원)
	# </span>
        for item in list:
                #에러처리하는 코드 추가 
                try:
                        title = item.text.strip()
                        #블럭 주석 처리: ctrl + /
                        if (re.search('애플워치', title)):
                                print(title)
                                f.write(title + "\n")
                except:
                        pass
        
#파일닫기
f.close()