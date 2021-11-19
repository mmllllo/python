# 리스트의 이해
# 리스트는 박스(변수)를 한줄로 붙인 뒤에 박스 전체의 이름을 지정
# 각각의 박스뒤에 [번호]를 사용 Ex 변수[0],변수[1].....
# 리스트이름 = [값1, 값2, 값3, ....]

#리스트와 반복문 실습
# 리스트 활용 전
a, b, c, d = 0, 0, 0, 0
hap = 0

a = int(input("첫번째 숫자 :"))
b = int(input("두번째 숫자 :"))
c = int(input("셋번째 숫자 :"))
d = int(input("넷번째 숫자 :"))

hap= a + b + c + d

print("합계 ==> %d"%hap)

#리스트 활용 후

aa = [0, 0, 0, 0]
hap = 0

aa[0] = int(input("첫번째 숫자 :"))
aa[1] = int(input("두번째 숫자 :"))
aa[2] = int(input("셋번째 숫자 :"))
aa[3] = int(input("넷번째 숫자 :"))

hap = aa[0] + aa[1] + aa[2] + aa[3]

print("합계 ==> %d"%hap)


#리스트의 일반적인 사용법
#리스트와 append() 함수 활용
#빈 리스트와 리스트의 추가
#비어있는 리스트를 만들고 '리스트이름.append(값)'함수로 리스트에 하나씩 추가

aa = []

aa.append(0)
aa.append(0)
aa.append(0)
aa.append(0)

print(aa)
#출력 결과
#[0, 0, 0, 0]

#for문 이용

aa = []

for i in range(0, 100) :
    aa.append(0)

print(len(aa))
