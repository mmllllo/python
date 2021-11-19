aa = []
max = 0
min = 0

b = int(input("몇개의 숫자를 비교 하겠습니까? "))
while True :
    for i in range(0,b) :
        aa.append(0)
        aa[i] = int(input(str(i + 1) + "번째 숫자 : "))
        print(aa)
        
        if aa[i] == aa[0] :
            max = aa[0]
            min = aa[0]
        if max < aa[i] :
            max = aa[i]
        if min > aa[i] :
            min = aa[i]

    print("max : ",max)
    print("min : ",min)
