## 함수 정의 부분
def dic_func(**para) : 
    # **는 딕셔너리형태로 매개변수 받겠다는 지정하는 의미
    print(para) # 딕셔너리 전체 출력
    print(type(para)) # para의 타입 출력
    print(para.keys) # para.keys()의 전체 출
    for k in para.keys() :
        print("%s ---> %d 명입니다."%(k,para[k]))

dic_func(아이오아이 = 11, 소녀시대 = 8, 걸스데이 = 4, AOA = 7)

