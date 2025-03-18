# function3.py
#수열 함수 
print(list(range(2000,2026)))
print(list(range(1,32))) 

#리스트 컴프리핸션(압축, 함축)
lst = list(range(1,11))
print([i**2 for i in lst if i > 5])

#필터링하는 함수
lst = [10,25,30]
iterL = filter(None, lst)
for item in iterL:
    print(item)
    
#조건에 해당하는 함수
def getBiggerThan20(i):
    return i > 20

iterL = filter(getBiggerThan20, lst)
for item in iterL:
    print(item)
    
print("==람다함수정의==")
iterL = filter(lambda x: x>20, lst)
for item in iterL:
    print(item)

#맵핑하는 함수:스칼라(단일값이 아닌 경우)
lst = [1,2,3]
def add10(i):
    return i + 10 

for item in map(add10, lst):
    print(item)

    
