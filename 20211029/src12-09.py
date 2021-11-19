from tkinter import*
window = Tk()
window.geometry("450x450")
window.title("애완동물 선택 하기")

#함수 정의 부분
filename3 = PhotoImage(file="E:\박규환\Python\gif\jeju13.gif")
imagelabe3 = Label(window,image=filename3)
def myFunc() :
    if var.get() == 1 :
        labelImage.configure(image = photo1 )
        labelText2.configure(text = "dog")
    elif var.get() == 2 :
        labelImage.configure(image = photo2)
        labelText2.configure(text = "cat")
    else :
        labelImage.configure(image = photo3)
        labelText2.configure(text = "rabbit")

#메인 코드 부분
labelText = Label(window, text = "좋아하는 동물 투표",fg = "blue",font =("궁서체",20))

var=IntVar()
rb1=Radiobutton(window, text="강아지", variable=var,value=1,command = myFunc)
rb2=Radiobutton(window, text="고양이", variable=var,value=2,command = myFunc)
rb3=Radiobutton(window, text="토끼", variable=var,value=3,command = myFunc)
buttonOk = Button(window, text = "사진 보기", command = myFunc)

photo1 = PhotoImage(file="E:\박규환\Python\gif\dog2.gif")
photo2 = PhotoImage(file="E:\박규환\Python\gif\cat2.gif")
photo3 = PhotoImage(file="E:\박규환\Python\gif\opopop.gif")
photo4 = PhotoImage(file="E:\박규환\Python\gif\MC20.gif")

labelImage = Label(window, width = 200, height = 200, image = photo4)
labelText2 = Label(window, text = "선택", fg="red",font =("궁서체",20))

imagelabe3.place(x=-2,y=-2)
labelText.pack(padx = 5, pady = 5)
rb1.pack(padx = 5, pady = 5)
rb2.pack(padx = 5, pady = 5)
rb3.pack(padx = 5, pady = 5)
buttonOk.pack(padx = 5, pady = 5)
labelImage.pack(padx = 5, pady = 5)
labelText2.pack(padx = 5, pady = 5)
window.mainloop()





