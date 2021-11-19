#함수 정의 부분
def calc(v1, v2, op) :
    result = 0
    if op == "+" :
        result = v1 + v2
    elif op == "-" :
        result = v1 - v2
    if op == "*" :
        result = v1 * v2
    if op == "/" :
        result = v1 / v2

    return result


##변수 선언 부분

res = 0
var1, var2, oper = 0, 0, ""

#메인 코드 부분
while 1: 
    try :
        oper = str(input("계산 입력 (+, -, *, /) : ",))
        if oper != "+"and"-"and"*"and"/" :
            print("주어진 값에서 입력해주세요.")
            continue
        var1 = int(input("첫 번째 숫자 입력 : "))
        var2 = int(input("두 번째 숫자 입력 : "))

        res = calc(var1, var2, oper)

        print(f"## 계산기 : {var1} {oper} {var2} = {res}")

    except ValueError:
        print("정수를 입력해주세요.")
        continue
