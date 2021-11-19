aa = []
hap = 0

b = int(input("몇개의 숫자를 더하겠습니까? "))
for i in range(0,b) :
    aa.append(0)
    aa[i] = int(input(str(i + 1) + "번째 숫자 : "))
    print(aa,hap)
    hap +=aa[i]
    print(hap)

print("합계==> %d"%hap)
