from tkinter import*
#random 함수를 불러오기 위한 모듈 임포트
import random

####전역 변수 초기화
x_speed = 20 #공의 x축 속도
y_speed = 0 #공의 y축 속도

#메인부
window = Tk()
window.title("MYPingPong")

###Table 클래스 생성
class Table :
    ###생성자
    def __init__(self,window,width,height,bg_color,net_color) :
        self.width = width
        self.height = height
        self.bg_color = bg_color
        self.net_color = net_color

        #Table 클래스 내에서 캔버스 생성
        self.canvas = Canvas(window, width = self.width, height = self.height, bg = self.bg_color)
        self.canvas.pack()

        self.canvas.create_line(self.width/2, 0, self.width/2, self.height, width = 2, fill = net_color, dash = (15,23))

    ##함수부
    #Canvas(Table)에 타원(Ball)을 추가하는 함수
    def draw_oval(self, oval):
        x1 = oval.x_posn
        x2 = oval.x_posn + oval.width
        y1 = oval.y_posn
        y2 = oval.y_posn + oval.height
        c = oval.color
        return self.canvas.create_oval(x1, y1, x2, y2 , fill = c)
    
    #Canvas(Table)에 직사각셩(배트)를 추가하는 함수
    def draw_rectangle(self,rectangle):
        x1 = rectangle.x_posn
        x2 = rectangle.x_posn + rectangle.width
        y1 = rectangle.y_posn
        y2 = rectangle.y_posn + rectangle.height
        c = rectangle.color
        return self.canvas.create_rectangle(x1, y1, x2, y2 , fill = c)
    
    #Canvas(Table)에 아이템 (공과 배트)을 조작할 수 있는 함수
    #coords()는 입력받은 값으로 속성값 업데이트하는 함수
    #변경된 위치값으로 공과 배트의 위치 변경
    def move_item(self, item, x1, y1, x2, y2):
        self.canvas.coords(item, x1, y1, x2, y2)

###Ball 클래스 생성
class Ball :
    ###생성자
    def __init__(self, table, width, height, color, x_speed, y_speed, x_posn, y_posn):
        self.width = width #공의 가로 사이즈
        self.height = height #공의 세로 사이즈
        self.x_posn = x_posn #공의 x좌표값
        self.y_posn = y_posn #공의 y좌표값
        self.color = color #공의 색상

        self.x_start = x_posn
        self.y_start = y_posn
        self.x_speed = x_speed
        self.y_speed = y_speed
        
        self.table = table
        self.circle = self.table.draw_oval(self)
    
    ###함수부
    # 공이 움직이는 부분
    def move_next(self):
        self.x_posn = self.x_posn + self.x_speed # 현재 공의 위치에 이동할 거리 x를 추가
        self.y_posn = self.y_posn + self.y_speed # 현재 공의 위치에 이동할 거리 y를 추가

        x1 = self.x_posn
        x2 = self.x_posn + self.width
        y1 = self.y_posn
        y2 = self.y_posn + self.height
        self.table.move_item(self.circle, x1, y1, x2, y2)

    #공의 초기 위치값 지정
    def start_position(self):
        self.x_posn = self.x_start
        self.y_posn = self.y_start

    #전역변수 x_speed의 값을 불러와서 공의 속도에 대입, 랜덤하게 생성된 값에 의해 + 또는 - 스피드 값이 적용
    def start_ball(self,x_speed , y_speed):
        self.x_speed = -x_speed if random.randint(0 , 1) else x_speed
        self.y_speed = -y_speed if random.randint(0 , 1) else y_speed
        self.start_position()

###Bat 클래스 생성
class Bat :
    ###생성자
    def __init__ (self, table, width, height, x_posn, y_posn, color, x_speed = 23, y_speed = 23):
        self.width = width
        self.height = height
        self.x_posn = x_posn
        self.y_posn = y_posn
        self.color = color

        self.x_start = x_posn
        self.y_start = y_posn
        self.x_speed = x_speed
        self.y_speed = y_speed

        #Table 클래스에 입력받은 매개변수 값 전달
        #Table의 draw_rectangle() 함수 실행
        self.table = table
        self.rectangle = self.table.draw_rectangle(self)
    
    ##함수부
    #배트를 위로 움직이는 함수
    def move_up(self, master): #이벤트를 처리하는 함수는 master 입력
        self.y_posn = self.y_posn - self.y_speed #y_speed의 값 만큼 y_posn 값을 뺌
        if(self.y_posn <= 0):#bat가 위 화면에 닿으면 더이상 올라가지않게 하는 코드
            self.y_posn = 0
        #self.y_posn -= self.y_speed
        x1 = self.x_posn
        x2 = self.x_posn + self.width
        y1 = self.y_posn #변경된 y_posn 값을 y1에 반영
        y2 = self.y_posn + self.height

        #변경된 값으로 아이템을 옮김
        #Table 클래스의 move_item() 함수를 실행
        self.table.move_item(self.rectangle, x1, y1, x2, y2)

    def move_down(self, master):
        self.y_posn = self.y_posn + self.y_speed #y_speed의 값 만큼 y_posn 값을 뺌
        if(self.y_posn >= 300):#bat가 위 화면에 닿으면 더이상 올라가지않게 하는 코드
            self.y_posn = 300
        #self.y_posn -= self.y_speed
        x1 = self.x_posn
        x2 = self.x_posn + self.width
        y1 = self.y_posn #변경된 y_posn 값을 y1에 반영
        y2 = self.y_posn + self.height

        self.table.move_item(self.rectangle, x1, y1, x2, y2)

    ##공과 배트의 충돌 감지 및 처리 함수
    def detect_collision(self,ball):
        collision_direction = "" #충돌 방향 저장
        collision = False       #충돌이 감지되면 True 로 바뀜
        feel = 5                #배트에서 공을 튕겨낸 다음 반사 각도와 반응 정도를 조정

        #배트 변수
        top = self.y_posn
        bottom = self.y_posn + self.height
        left = self.x_posn
        right = self.x_posn + self.width
        v_center = top + (self.height/2) #배트의 탑에서 배트의 높이를 2로 나눈 값 더하면 세로 중간
        h_center = left + (self.width/2) #배트의 레프트에서 배트의 넓이를 2로 나눈 값 더하면 가로 중간

        #공 변수
        top_b = ball.y_posn
        bottom_b = ball.y_posn + ball.height
        left_b = ball.x_posn
        right_b = ball.x_posn + ball.width
        r = (right_b - left_b)/2 #반지름
        v_center_b = top_b + r #공의 탑에서 반지름을 더하면 세로 중간
        h_center_b = left_b + r #공의 왼쪽에서 반지름을 더하면 가로 중간
        
        #공의 바닥(y)이 배트의 탑(y)보다 크고, 공의 탑(y)이 배트의 바닥(y)보다 작고
        #공의 오른쪽이 배트의 왼쪽보다 크고, 공의 왼쪽이 배트의 오른쪽 보다 작을때 충돌
        if((bottom_b > top) and (top_b < bottom) and (right_b > left) and (left_b < right)):
            collision = True #collision의 값 변경
            print("충돌")
        #만약 충돌했다면 어느 방향으로 충돌했는지 collision_direction에 저장
        if(collision): #만약 collision이 True라면, 즉 충돌했다면
            #공의 오른쪽 부분이 배트의 오른쪽 부분보다 크고, 공의 왼쪽 부분이 배트의 오른쪽 보다 작다면 배트의 동쪽에서 공이 충돌
            if((right_b > right) and (left_b <= right) and (top_b > top-r) and (bottom_b < bottom+r)):
                collision_direction = "E"
                #abs() 함수는 숫자의 부호를 제거하는 함수, 속도 값을 얻는데 사용
                #abs() 함수는 공이 배트의 어느 부분에 충돌했는지에 따라 공이 튀는 방향 바꿈
                ball.x_speed = abs(ball.x_speed) #공이 양수의 값, 즉 오른쪽으로 이동

                #공의 중심이 배트의 중심에서 얼마나 먼 거리에서 충돌이 발생했는지 계산하여 y 좌표값에 적용
                #공의 중심이 배트의 중심보다 y 좌표값이 적은 위치(높은 위치)에서 부딫힐 경우 adjustment는 - 값이 되어 공은 사선 위로 이동
                #공의 줌심이 배트의 중심보다 y 좌표값이 큰 위치(낮은 위치) 에서 부딫힐 경우 adjustment는 + 값이 되어 공은 사선 아래로 이동
                adjustment = (-(v_center - v_center_b))/(self.height/2)
                print(adjustment)
                ball.y_speed = feel * adjustment
            
            #공의 왼쪽 부분이 배트의 왼쪽 부분보다 작고, 공의 오른쪽 부분이 배트의 왼쪽보다 크다면 배트의 서쪽에서 공이 충돌
            elif ((left_b < left) and (right_b >= left) and (top_b > top-r) and (bottom_b < bottom+r)):
                    collision_direction = "W"
                    ball.x_speed = -abs(ball.x_speed)

                    adjustment = (-(v_center - v_center_b))/(self.height/2)
                    print(adjustment)
                    ball.y_speed = feel * adjustment

            return (collision, collision_direction)

###game_flow() 함수부
def game_flow():
    #공을 일정 시간마다 움직임
    my_ball.move_next()
    window.after(30,game_flow) #30밀리초마다 game_flow 함수 실행, ex 5초는 500

    #공이 배트에 닿았는지 충돌 확인, 두배트에 대해 detect_collision() 함수 실행
    bat_L.detect_collision(my_ball)
    bat_R.detect_collision(my_ball)

### restart_game() 함수부
#게임을 재시작하는 함수
def restart_game(master):
    my_ball.start_ball(x_speed = x_speed, y_speed = y_speed)

#Table 클래스를 사용해서 테이블 생성
my_Table = Table(window, 600, 400, "black", "green")
###공 생성
#Ball(self, table, width, height, color, x_speed, y_speed, x_posn, y_posn)
my_ball = Ball(table = my_Table, x_speed = 0, y_speed = 0, width = 24, height = 24, color = "red", x_posn = 288, y_posn = 188)
my_ball.move_next()

###배트 생성
# Bat 클래스로부터 배트를 주문
# Bat(self,table,width,height, x_posn, y_posn, color, x_speed = 25, y_speed= 25)
bat_L = Bat(table = my_Table, width = 15, height = 100, x_posn =20, y_posn= 150, color = "blue")
bat_R = Bat(table = my_Table, width = 15, height = 100, x_posn =565, y_posn= 150, color = "yellow")

### 함수의 실행부
game_flow()

###restart_game 함수 실행부
#스페이스바를 눌러 게임 시작 또는 재시작
window.bind("<space>",restart_game)

### 배트를 제어하기 위한 키이벤트 및 연결될 함수 지정
#window.bind("<키명>",함수명)
window.bind("a",bat_L.move_up)
window.bind("z",bat_L.move_down)
window.bind("<Up>",bat_R.move_up)
window.bind("<Down>",bat_R.move_down)

window.mainloop()