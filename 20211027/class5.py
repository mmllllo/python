##클래스 선언
class Car :
    color = ""
    speed = 0
    count = 0

    def __init__(self) :#생성자
        self.speed = 0#인스턴스 변수
        Car.count += 1#클래스 변수(클래스 전체에서 적용)

#변수 선언
myCar1,myCar2 = None, None

#메인 코드 부분
myCar1 = Car()
myCar1.speed = 30
print("자동차1의 현재 속도는 %d km, 생산된 자동차 숫자는 총 %d대입니다."%(myCar1.speed, Car.count))

myCar2 = Car()
myCar2.speed = 60
print("자동차2의 현재 속도는 %d km, 생산된 자동차 숫자는 총 %d대입니다."%(myCar2.speed, Car.count))