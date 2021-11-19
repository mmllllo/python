#tkinter는 파이썬에서 GUI관련 무듈을 제공해주는 표준 윈도우 라이브러리
#위젯(Widget) 윈도우 창에 나올 수 있는 문자,버튼,체크박스,라디오버튼 등을 말함
from tkinter import*
#Tk()는 기본이 되는 윈도우를 반환,루트 윈도우(Root Window),또는 베이스 윈도우(Base Window)
window=Tk()
#윈도우 창에 제목 표시
window.title("윈도우 창 연습")
#윈도우 창 크기 지정
window.geometry("400x100")
#윈도우 크기 변경 가능 여부설정, TRUE/FALSE or 1/0
window.resizable(width = FALSE, height = FALSE)

#라벨은 문자를 표현할 수 있는 위젯
#위젯은 생성하고 디스플레이하는 2스텝으로 진행

#화면을 구성하고 처리
#윈도우 창에 키보드 누르기, 마우스 클릭 등  다양한 이벤트를 처리
window.mainloop()