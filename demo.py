# demo.py 
print("Hello VS Code")

result = 3 + 5 
print(result)


#디버깅: 논리적 오류를 찾는 도구 
#반복문 
#중단점(Break point)
for i in [1,2,3]:
    print(i)

#튜플
tp = (10, 20, 30)
print(tp)
print(type(tp))

#함수를 정의
def calc(a,b):
    return a+b, a*b 

#함수를 호출
print(calc(3,4))

args = (5,6)
print(calc(*args))

#형식 변환 
a = set([1,2,3])
print(a)
print(type(a))
b = list(a)
b.append(4)
print(b)
print(type(b))


