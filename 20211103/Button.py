from tkinter import*
window = Tk()
window.geometry("800x600")
"""
#버튼 생성
button1 = Button(window, text = "버튼1")
button2 = Button(window, text = "버튼2")
button3 = Button(window, text = "버튼3")

#버튼 출력
button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
"""
'''
#반복문과 리스트를 활용하여 소스코드 수정하기
button = [None]*7
for i in range(2) :
    for j in range (1,4):
        button[j] = Button(window,text = "버튼"+str(j))
        button[j].place(x=j*45-40,y=i*30)
'''
'''
#버튼 생성
button1 = Button(window, text = "버튼1")
button2 = Button(window, text = "버튼2")
button3 = Button(window, text = "버튼3")
button4 = Button(window, text = "버튼4")
button5 = Button(window, text = "버튼5")
button6 = Button(window, text = "버튼6")

#버튼 출력
button1.place(x=0,y=0)
button2.place(x=50,y=0)
button3.place(x=100,y=0)
button4.place(x=0,y=30)
button5.place(x=50,y=30)
button6.place(x=100,y=30)
'''
button = [None]*12
xPos, yPos = 0,0

i = 0
for y in range(0,3):
    for x in range(0,4):
        button[i] = Button(window, text= "버튼"+str(i+1))
        button[i].place(x=xPos , y=yPos)
        xPos += 50
        i += 1
    xPos = 0
    yPos += 30

window.mainloop()