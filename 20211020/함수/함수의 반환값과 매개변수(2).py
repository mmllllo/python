## 함수 정의 부분
def para2_func(v1,v2) :
    result = 0
    result = v1 + v2
    return result

def para3_func(v1, v2, v3) :
    result = 0
    result = v1 + v2 + v3
    return result
#매개변수의 개수를 정해놓는 방법


##변수 선언 부분
hap = 0

##메인 코드 부분
hap = para2_func(10,20)
print("매개변수 2함수 호출 결과 == > %d" %hap) 
hap = para3_func(10,20,30)
print("매개변수 3함수 호출 결과 == > %d" %hap) 
