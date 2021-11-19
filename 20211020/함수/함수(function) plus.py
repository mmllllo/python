# 함수의 개념
# 함수는 파이썬 프로그램 자체에서 제공하지만, 사용자가 직접 만들어서 사용하기도 함

## 함수 정의 부분
def plus(v1, v2) : #def 함수면(매개변수1, 매개변수2...)
    result = 0
    result = v1 + v2
    return result

## 변수 선언 부분
hap = 0

## 메인 코드 부분
# 함수의 실행부
while 1 :
    a = int(input("더 할 첫번째 수를 입력해주세요: "))
    b = int(input("더 할 두번째 수를 입력해주세요: "))
    hap=plus(a,b)
    print(f"{a}과{b}의 plus()함수 결과는 %d" %hap)
    print()
    c = str(input("종료를 원하시면 c를 입력해주세요. \n계속 할시 엔터 키를 입력해주세요."))
    if c == "c" :
        break

