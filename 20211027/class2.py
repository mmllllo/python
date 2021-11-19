#클래스 정의 부분
class Car :
    color = ""
    speed = 0
#생성자 추가,인스턴스를 생성하면 무조건 호출되는 메소드
    def __init__(self) :
        self.color = "빨강"
        self.speed = 0

    def upSpeed(self,value) :
        self.speed += value
    
    def downSpeed(self,value) :
        self.speed -= value

#메인 코드 부분
myCar1 = Car()
myCar2 = Car()

print("자동차1의 색상은 %s이며, 현재속도는 %d km 입니다."%(myCar1.color,myCar1.speed))

print("자동차2의 색상은 %s이며, 현재속도는 %d km 입니다."%(myCar2.color,myCar2.speed))