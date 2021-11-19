from tkinter import*

window = Tk()
window.geometry("800x600")
'''
filename1 = PhotoImage(file="E:\박규환\Python\gif\puz1.gif")
imagelabel = Label(window,image=filename1)
imagelabel.pack(side=LEFT)

filename2 = PhotoImage(file="E:\박규환\Python\gif\puz2.gif")
imagelabe2 = Label(window,image=filename2)
imagelabe2.pack(side=LEFT)

filename3 = PhotoImage(file="E:\박규환\Python\gif\puz3.gif")
imagelabe3 = Label(window,image=filename3)
imagelabe3.pack(side=LEFT)
'''
#반복문과 리스트를 결합하여 이미지 위젯을 순서대로 표시하기
#빈 리스트 선언
filename = [None]*10
imagelabel = [None]*10

for i in range (1,10,1) :
    filename[i] = PhotoImage(file="E:\박규환\Python\gif\puz"+str(i)+".gif")
    imagelabel[i] = Label(window,image=filename[i])
    imagelabel[i].pack(side=LEFT)

window.mainloop()