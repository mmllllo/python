from tkinter import*
from tkinter import messagebox
#함수 정의 부분
"""
def clickLeft(event) :
    messagebox.showinfo("마우스","마우스 왼쪽 버튼이 클릭됨")
def clickRight(event) :
    messagebox.showinfo("마우스","마우스 오른쪽 버튼이 클릭됨")
def clickmid(event) :
    messagebox.showinfo("마우스","마우스 가운데 버튼이 클릭됨")
"""   
def clickImage(event) :
    messagebox.showinfo("마우스","토끼다 토끼야 토끼다 토끼야 토끼다 토끼야 토끼다 토끼야 토끼다 토끼야 토끼다 토끼야 토끼다 토끼야 토끼다 토끼야 토끼다 토끼야 토끼다 토끼야 토끼다 토끼야 토끼다 토끼야 토끼다 토끼야 토끼다 토끼야 토끼다 토끼야")  
def leaveImage(event) :
    messagebox.showinfo("마우스","간다간다간다간다간다간다간다간다간다간다간다간다간다간다간다간다간다간다간다간다")   
#메인 코드 부분
window = Tk()
window.geometry("400x400")

photo = PhotoImage(file = "gif/rabbit2.gif")
label1 = Label(window, image = photo)

label1.bind("<Enter>",clickImage)
label1.bind("<Leave>",leaveImage)
"""
window.bind("<Button-1>",clickLeft)
window.bind("<Button-2>",clickmid)
window.bind("<Button-3>",clickRight)
"""
label1.pack( expand = 1, anchor = CENTER)

window.mainloop()
