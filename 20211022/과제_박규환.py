a = [3,18,79,61,50,24,38,45]

x=int(input("탐색할 값을 입력하세요 : "))

def search_list(a,x):
    n=len(a)
    for i in range(0,n):
        if x ==a[i]:
            return i+1
    return -1
    
print("%d값은 %d위치에 있습니다."%(x,search_list(a,x)))
