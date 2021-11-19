from tkinter import*
from time import*

#변수 선언 부분
fnameList = ["bg.png","bg1.png","bg2.png","bg3.png","bg4.png"]
photoList = [None] * 6
num = 0 #리스트의 인덱스 값을 저장하는 변수


#함수 선언 부분
def clickNext() :
    global num
    num += 1
    if num > 5 :
        num = 0
    photo = PhotoImage(file = "gif/"+fnameList[num])
    imagelabel.configure(image = photo)
    imagename.configure(text = fnameList[num])
    pLabel.image = photo

def clickPrev() :
    global num
    num -= 1
    if num < 0 :
        num = 5
    photo = PhotoImage(file = "gif/"+fnameList[num])
    imagelabel.configure(image = photo)
    imagename.configure(text = fnameList[num])
    pLabel.image = photo

def pageUp(event) :
    clickNext()

def pageDown(event) :
    clickPrev()

#메인 코드 부분
window = Tk()
window.geometry("1240x800")
window.title("사진 앨범 보기")
bg = PhotoImage(file = "gif/bg.png")


window.bind("<Prior>",pageUp)
window.bind("<Next>",pageDown)
photo1 = PhotoImage(file = "gif/left-arrow.png")
photo2 = PhotoImage(file = "gif/right-arrows.png")
photo3 = PhotoImage(file = "gif/horse.png")

imagelabel = Label(window, image = bg)
photo = PhotoImage(file = "gif/"+fnameList[0])
pLabel = Label(window, image = photo3)
imagename = Label(window, text = "jeju1")
btnPrev = Button(window, image = photo1  , command = clickPrev)
btnNext = Button(window, image = photo2  , command = clickNext)


imagelabel.place (x = -2, y = -2)
btnPrev.place (x = 800, y = 470)
btnNext.place (x = 900, y = 470)
imagename.place (x = 860, y = 470)
pLabel.place ( x = 800, y = 10)

window.mainloop()
