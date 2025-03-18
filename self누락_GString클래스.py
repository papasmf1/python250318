#전역변수 
strName = "Not Class Member"

#클래스 정의 
class DemoString:
    #초기화 메서드 
    def __init__(self):
        #인스턴스 멤버 변수 
        self.strName = "" 
    def set(self, msg):
        self.strName = msg
    def print(self):
        #버그 발생 
        print(self.strName)

#인스턴스 생성 
d = DemoString()
d.set("First Message")
d.print()
