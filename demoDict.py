# demoDict.py 
color = {"apple":"red", "banana":"yellow"}
print(len(color))
#검색
print(color["apple"])
#입력 
color["cherry"] = "red"
print(color)
#삭제
del color["apple"]
print(color)

#반복문 
for item in color.items():
    print(item)

print("key, value 따로 출력")
for k,v in color.items():
    print(k,v)



