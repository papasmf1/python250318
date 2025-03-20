# DemoForm2.py 
# DemoForm2.ui + DemoForm2.py
import sys 
from PyQt5.QtWidgets import * 
from PyQt5 import uic
#웹크롤링 
from bs4 import BeautifulSoup
#웹서버에 요청 
import urllib.request
#특정 문자열 검색 
import re 

#디자인 파일을 로딩:파일명 수정 
form_class = uic.loadUiType("DemoForm2.ui")[0]

#윈도우 클래스 정의:상속받는 클래스명 변경 
class DemoForm(QMainWindow, form_class): 
    def __init__(self): 
        super().__init__() 
        self.setupUi(self)
    #슬롯메서드 추가
    def firstClick(self):
        hdr = {'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1'}
        f = open("clien.txt", "wt", encoding="utf-8")
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
        self.label.setText("중고장터 검색 완료")
    def secondClick(self):
        self.label.setText("두번째 버튼을 클릭했음~~")
    def thirdClick(self):
        self.label.setText("세번째 버튼을 클릭함 ㅋㅋ")

#진입점 체크 
if __name__ == "__main__": 
    app = QApplication(sys.argv) 
    demoWindow = DemoForm() 
    demoWindow.show() 
    app.exec_()