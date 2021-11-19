l = [5,3,8,4,7,1,9,2,6]

for j in range(len(l)) :
    k = len(l) - j
    for i in range(1, k) :
        if l[i-1] >= l[i]:
            temp = l[i-1]
            l[i-1] = l[i]
            l[i] = temp
print(l)