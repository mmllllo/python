#tkinter는 파이썬에서 GUI관련 무듈을 제공해주는 표준 윈도우 라이브러리
from tkinter import*
from tkinter import messagebox
#Tk()는 기본이 되는 윈도우를 반환,루트 윈도우(Root Window),또는 베이스 윈도우(Base Window)
window=Tk()
##window2=Tk()
window.title("윈도창 연습")
##window2.title("가즈아")
#step1. 라벨 위젯을 생성
label1 = Label(window, text = "SWEDU~~ Python을")
label2 = Label(window, text ="열심히", font = ("궁서체",30),fg = "blue")
#anchor는 위젯의 위치 지정, N,NE, E, SE, S, SW, W, NW, CENTER 등이며 기본값은 CENTER
label3 = Label(window, text = "공부 중입니다.", bg = "magenta", width = 20, height = 5, anchor = SE)
#step2. 라벨 위젯을 화면에 표시
#pack()함수를 호출하여 화면에 디스플레이 됨
label1.pack()
label2.pack()
label3.pack()
#2. 이미지 위젯 표시/
#step1. 이미지 불러옴
filename=PhotoImage(file="E:\박규환\Python\gif\dog.gif")
filename2=PhotoImage(file="E:\박규환\Python\gif\dog2.gif")
filename3=PhotoImage(file="E:\박규환\Python\gif\jeju2.gif")
#step2. 라벨 위젯을 생성
imagelabel3 = Label(window,image=filename3)
imagelabel = Label(window,image=filename)
imagelabel2 = Label(window,image=filename2)


#step3. 라벨 위젯을 화면에 표시
imagelabel3.place(x=-2,y=-2)
imagelabel.place(x=100,y=150)
imagelabel2.place(x=300,y=150)

#사용자 정의 함수 만들기
def myFunc():
    messagebox.showinfo("강아지 버튼","강아지가 귀엽죠?")
#3.버튼 위젯 표시
#step1. 버튼 위젯을 생성
button1=Button(window,text="파이썬 종료",fg= "red", command=quit)#버튼에 텍스트 표시
button1=Button(window,image=filename2,fg= "red", command=myFunc)#버튼에 이미지 표시

#step2. 버튼 위젯을 화면에 표시
button1.pack()

#화면을 구성하고 처리

window.mainloop()
##window2.mainloop()