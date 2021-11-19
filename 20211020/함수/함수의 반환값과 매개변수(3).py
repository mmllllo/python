## 함수 정의 부분
def para_func(v1,v2,v3 = 0) :
    #v3의 기본값을 0으로 지정시 메인코드에서 기본값을 안 주어도 실행.
    result = 0
    result = v1 + v2 + v3
    return result
#매개변수에 기본값을 설정해놓는 방법


##변수 선언 부분
hap = 0

##메인 코드 부분
hap = para_func(10,20)
print("매개변수 2함수 호출 결과 == > %d" %hap) 
hap = para_func(10,20,30)
print("매개변수 3함수 호출 결과 == > %d" %hap) 
