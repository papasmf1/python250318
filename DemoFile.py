#DemoFile.py 
#새로운 파일에 쓰기 
#탭코딩(바이브 코딩)
f = open("demo.txt", "wt", encoding="utf-8")
f.write("Hello, Python\n두번째\n세번째\n")
f.close()

#기존 파일을 읽기 
f = open("demo.txt", "rt", encoding="utf-8")
text = f.read() 
f.close()
print(text)


