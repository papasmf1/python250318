# DemoSQL.py 
#SQLite3를 사용하는 데모 
import sqlite3

#연결객체를 생성(물리적인 파일에 저장)
#정상적으로 커밋을 한 경우 
con = sqlite3.connect('c:\\work\\sample.db')
#커서 객체를 생성   
cur = con.cursor()
#테이블을 생성
cur.execute('create table PhoneBook (Name text, PhoneNum text);')
#1건 데이터를 입력
cur.execute("insert into PhoneBook values ('Derick', '010-1234-5678');")
#입력 파라메터 처리
name = '홍길동'
phoneNumber = '010-1234-5678'
cur.execute("insert into PhoneBook values (?, ?);", (name, phoneNumber))
#여러건 입력:2차원 데이터-2행2열  
datalist = (('이순신', '010-1234-5678'), ('전우치', '010-1234-5678'))
cur.executemany("insert into PhoneBook values (?, ?);", datalist)

#데이터를 조회
cur.execute("SELECT * FROM PhoneBook;")
#선택한 블럭을 주석 처리: Ctrl + /
for row in cur:
    print(row)

#정상적으로 완료
con.commit()


