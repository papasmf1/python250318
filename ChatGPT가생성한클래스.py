class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    
    def printInfo(self):
        print(f"ID: {self.id}, Name: {self.name}")

class Manager(Person):
    def __init__(self, id, name, title):
        super().__init__(id, name)
        self.title = title
    
    def printInfo(self):
        super().printInfo()
        print(f"Title: {self.title}")

class Employee(Person):
    def __init__(self, id, name, skill):
        super().__init__(id, name)
        self.skill = skill
    
    def printInfo(self):
        super().printInfo()
        print(f"Skill: {self.skill}")

# 테스트 코드
def test():
    print("--- Test 1: Person 생성 ---")
    p1 = Person(1, "Alice")
    p1.printInfo()
    
    print("--- Test 2: Manager 생성 ---")
    m1 = Manager(2, "Bob", "Team Leader")
    m1.printInfo()
    
    print("--- Test 3: Employee 생성 ---")
    e1 = Employee(3, "Charlie", "Python")
    e1.printInfo()
    
    print("--- Test 4: Person 다수 생성 ---")
    p2 = Person(4, "David")
    p3 = Person(5, "Eve")
    p2.printInfo()
    p3.printInfo()
    
    print("--- Test 5: Manager 다수 생성 ---")
    m2 = Manager(6, "Frank", "HR Manager")
    m3 = Manager(7, "Grace", "Project Manager")
    m2.printInfo()
    m3.printInfo()
    
    print("--- Test 6: Employee 다수 생성 ---")
    e2 = Employee(8, "Henry", "Java")
    e3 = Employee(9, "Isabel", "C++")
    e2.printInfo()
    e3.printInfo()
    
    print("--- Test 7: 상속 관계 확인 ---")
    print(isinstance(m1, Person))  # True
    print(isinstance(e1, Person))  # True
    print(isinstance(p1, Manager))  # False
    print(isinstance(p1, Employee))  # False
    
    print("--- Test 8: ID 중복 확인 ---")
    p4 = Person(1, "Jack")  # ID 중복 테스트
    p4.printInfo()
    
    print("--- Test 9: Manager 정보 출력 확인 ---")
    m4 = Manager(10, "Karen", "CTO")
    m4.printInfo()
    
    print("--- Test 10: Employee 정보 출력 확인 ---")
    e4 = Employee(11, "Leo", "JavaScript")
    e4.printInfo()

# 테스트 실행
test()
