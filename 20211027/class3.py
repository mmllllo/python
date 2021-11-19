#클래스 정의 부분
class Car :
    color = ""
    speed = 0
#생성자 추가,인스턴스를 생성하면 무조건 호출되는 메소드
#매게변수를 입력받아 생성자 실행
    def __init__(self,value1,value2) :
        self.color = value1
        self.speed = value2

    def upSpeed(self,value) :
        self.speed += value
    
    def downSpeed(self,value) :
        self.speed -= value

#메인 코드 부분
myCar1 = Car("빨강",0) #myCar1 인스턴스 생성, 매게변수가 있는 클래스
myCar2 = Car("노랑",10)

print("자동차1의 색상은 %s이며, 현재속도는 %d km 입니다."%(myCar1.color,myCar1.speed))

print("자동차2의 색상은 %s이며, 현재속도는 %d km 입니다."%(myCar2.color,myCar2.speed))