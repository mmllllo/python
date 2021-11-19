## 함수 정의 부분
def para_func(*para) : # *의 뜻은 가변 매개변수(변수가 몇개가 들어올지 모른다.)
    # *는 튜플형태로 매개변수 받겠다는 지정하는 의미
    print(para)
    print(type(para))
    result = 0
    for num in para :
        result = result + num

    return result
#매개변수의 숫자를 정해놓지 않는 방법 -가변 매개변수(Arbitrary Argument List)

##변수 선언 부분
hap = 0

##메인 코드 부분
hap = para_func(10,20)
print("매개변수 2함수 호출 결과 == > %d" %hap) 
hap = para_func(10,20,30)
print("매개변수 3함수 호출 결과 == > %d" %hap)
