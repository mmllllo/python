from tkinter import*

window = Tk()
window.geometry("210x210")

#변수 선언 부분
fnameList=["gif/puz1.gif"]
'''
for i in range(2,10):
    fnameList.append("gif/puz"+str(i)+".gif")
    print(fnameList)

#이미지 생성
photoList = [None] * 9
for i in range(0,9):
    photoList[i] = PhotoImage(file = fnameList[i])

button = [None] * 9
xPos , yPos = 0,0

i = 0
print(button)
for y in range (0,3):
    xPos = 0

    for x in range(0,3):
        button[i] = Button(window,image = photoList[i])
        button[i].place(x=xPos, y=yPos)
        xPos += 70
        i += 1
    yPos += 70
'''
button = [None]*10

photoList = [None] * 10
x, y = 0,0
xPos, yPos = 0,0

i=1

for y in range(0,3):
    for x in range (0,3):
        fnameList.append("gif/puz"+str(i)+".gif")
        photoList[i] = PhotoImage(file = fnameList[i])
        
        button[i] = Button(window,image = photoList[i])
        button[i].place(x=xPos, y=yPos)
        xPos += 70
        i += 1
    xPos = 0
    yPos += 70


window.mainloop()
