#부모 클래스 정의 
class Person:
    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber
    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(self.name, self.phoneNumber))

#자식 클래스 정의(대학생) 
class Student(Person):
    #상속받고 재정의(덮어쓰기, override)
    def __init__(self, name, phoneNumber, subject, studentID):
        #부모의 생성자 호출(super, base라는 키워드 제공)
        Person.__init__(self, name, phoneNumber)
        self.subject = subject
        self.studentID = studentID
    #상속받고 재정의 
    def printInfo(self):
        print("Info(이름:{0}, 전화번호: {1})".format(
            self.name, self.phoneNumber))
        print("Info(학과:{0}, 학번: {1})".format(
            self.subject, self.studentID))


p = Person("전우치", "010-222-1234")
s = Student("이순신", "010-111-1234", "소프트웨어공학", "23001")
p.printInfo()
s.printInfo()



