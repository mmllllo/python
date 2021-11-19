#다차원 리스트
'''
list1=[]
list2=[]
value=1
'''
'''
for i in range(0,3) :
    for k in range(0,4):
        list1.append(value)
        value+=1
    list2.append(list1)
    list1=[]

for i in range(0,3) :
    for k in range(0,4) :
        print("%3d"% list2[i][k], end="")
    print("")
'''
#1차원 배열
'''
for i in range(0,4) :
    list1.append(i)
    print(list1)
'''
#2차원 배열
list1=[]#내부배열
list2=[]#외부배열
value=1#배열의 값을 위한 변수

for i in range(0,3):#외부 배열을 위한 반복문,3번 반복
    for k in range(0,4):#내부 배열을 위한 반복문 ,4번 반복
        list1.append(value)#빈 리스트에 value값을 추가
        value+=1#value 1씩 증가
        print(list1)
    list2.append(list1)# 외부 배열에 내부 배열을 추가
    list1 = []#내부 배열 비우기
#print(list1)
#print(list2)b

#2차원 리스트의 값을 출력하기, 하나하나 출력하기
for i in range(0,3):
    for k in range(0,4):
        print("%3d"%list2[i][k],end="")#3칸으로 출력하고 한 칸 띄우기
    print("")