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
f = open("c:\\work\\todayHumor.txt", "wt", encoding="utf-8")
#페이징하는 URL주소를 조립 
for n in range(1,11):
        #오늘의 유머 베스트 게시판
        data ='https://www.todayhumor.co.kr/board/list.php?table=bestofbest&page=' + str(n)
        print(data)
        #웹브라우져 헤더 추가 
        req = urllib.request.Request(data, \
                                    headers = hdr)
        data = urllib.request.urlopen(req).read()
        page = data.decode('utf-8', 'ignore')
        soup = BeautifulSoup(page, 'html.parser')
        list = soup.find_all('td', attrs={'class':'subject'})
        # <td class="subject">
        # <a href="/board/view.php?table=bestofbest">라떼 러닝크루</a>
        # <span class="list_memo_count_span"> [22]</span>  <span style="margin-left:4px;"><img src="http://www.todayhumor.co.kr/board/images/list_icon_photo.gif" style="vertical-align:middle; margin-bottom:1px;"> </span> </td>

        for item in list:
                #에러처리하는 코드 추가 
                try:
                        title = item.find('a').text.strip() 
                        #print(title)
                        #블럭 주석 처리: ctrl + /
                        if (re.search('한국', title)):
                                print(title)
                                f.write(title + "\n")
                except:
                        pass
        
#파일닫기
f.close()