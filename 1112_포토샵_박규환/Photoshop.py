#미니 포토샵
#포토샵과 같은 소프트웨어를 "영상처리(Image Processing)프로그램"이라 함
#원칙적으로 영상처리에 대한 이론과 알고리즘을 익힌 후 미니 포토샵 프로그램을 작성하면 좋음
#현실적으로 이론은 배제하고 화면에 구현되는 것 위주로 진행

#주의 사항1 .이미지 파일명이나 저장된 경로에 한글이 들어가면 안됨
#주의 사항2. 이미지 크기는 가로와 세로가 동일해야함
#주의 사항3. 처리하는 속도가 다소 오래 걸림

#사용할 라이브러리 또는 모듈을 임포트
from tkinter import*
from tkinter.filedialog import*     #파일 입출력을 위한 모듈
from tkinter.simpledialog import*   #숫자나 문자를 입력 받기 위한 모듈
from wand.image import*
#설치한 이미지 처리 기능을 제공하는 이미지매직의 라이브러리 임포트
#GIF 뿐 아니라 JPG,PNG 같은 이미지를 모두 처리하기 위해 외부 라이브러리 이미지 매직 사용

#모든 함수들이 공통적으로 사용할 전역 변수 선언
window,canvas,paper = None, None, None
photo,photo2 = None, None #photo는 처음 불러들인 원본 이미지,  photo2는 처리 결과를 저장할 사본 이미지
oriX,oriY = 0, 0 #원본 이미지의 폭과 높이를 저장하는 함수

#함수 정의 부분, 각 메뉴를 선택할 때 실행될 함수 선언
#displayImage(이미지, 가로사이즈, 세로사이즈) : 이미지를 화면에 출력하는 함수
def displayImage(img, width, height) :
    global window,canvas,paper,photo,photo2,oriX,oriY
    #이전 캔버스가 존재한다면 새 캔버스와 그 위에 새 종이를 생성하여 깨끗하게 처리한 후 처리된 이미지 출력
    #이전 캔버스가 존재한다면 이전 캔버스를 삭제하여 기존에 이미지가 출력된 캔버스를 깨끗하게 처리
    window.geometry(str(width)+"x"+str(height))
    if canvas != None :
        canvas.destroy()

    #새 캔버스 생성, 처리된 이미지의 가로 세로 사이즈대로 생성
    #캔버스의 흰색 테두리 없애기, bd = 0, highlightthickness = 0
    canvas = Canvas(window, width = width , height = height, bg="#626262", bd = 0,highlightthickness = 0)
    #새 캔버스에 붙일 종이(paper)생성 처리된 이미지의 가로 세로 사이즈대로 생성
    paper = PhotoImage(width = width, height = height)
    #새 캔버스에 종이 (paper)를 붙임 (차후 그 종이 위에 처리된 이미지를 출력)
    #생성될 페이퍼의 위치는 캔버스의 가로 세로 사이즈의 중간 위치
    canvas.create_image((width/2, height/2),image = paper, state = "normal")
    #새 캔버스와 새 종이 위에 처리된 이미지를 출력
    #make_blob(format = None)는 이미지를 바이너리 코드로 변환해주는 함수, 배열의 형태로 저장
    #흰종이에 사진을 출력하기 위해 이미지 파일의 모든 점(픽셀)에 접근
    blob = img.make_blob(format = "RGB")
    print(blob)
    for i in range(0,width) :
        for k in range(0,height) :
            r = blob[(i*3*width)+(k*3) + 0] #blob [0], blob [3], blob[6], blob[9]....의 값을 r에 저장
            g = blob[(i*3*width)+(k*3) + 1] #blob [1], blob [4], blob[7], blob[10]....의 값을 g에 저장
            b = blob[(i*3*width)+(k*3) + 2] #blob [2], blob [5], blob[8], blob[11]....의 값을 b에 저장
            #paper에 칼라로 점을 찍어줌, 세로로 높이만큼 찍고 가로를 너비만큼 반복
            paper.put("#%02x%02x%02x" %(r,g,b), (k,i))
    #처리된 결과 이미지의 픽셀을 찍어둔 종이paper가 붙여있는 캔버스를 화면에 출력
    canvas.pack()


def func_open() :
    #전역 변수 선언
    global window,canvas,paper,photo,photo2,oriX,oriY
    readFp = askopenfilename(parent = window, filetypes =(("모든 그림 파일","*.jpg;*.jpeg;*.bmp;*.png;*.tif;*.gif"),("모든 파일","**")))
    #photo는 처음 불러들인 원본 이미지
    photo = Image(filename = readFp)
    oriX = photo.width  #원본 이미지의 가로 사이즈를 oriX에 저장
    oriY = photo.height #원본 이미지의 세로 사이즈를 oriY에 저장
    #photo2는 처리 결과를 저장할 변수
    photo2 = photo.clone() #원본 이미지의 photo를 복사하여 photo2에 저장
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)#화면에 이미지를 출력하는 dispalyImage()함수 호출

def func_save() :
    global window,canvas,paper,photo,photo2,oriX,oriY #전역 변수 선언
    #photo2는 func_open() 함수를 실행하면 생성됨
    #파일을 열지 않았다면 저장하기를 눌렀을 때 함수를 빠져나감
    if photo2 == None :
        return
    #대화 상자로부터 넘겨받은 파일의 정보를 saveFp에 저장
    saveFp = asksaveasfile(parent = window, mode = "w",defaultextension = ".jpg", filetypes =(("JPG파일","*.jpg;*.jpeg  "),("모든 파일","*.*")))
    savePhoto = photo2.convert("jpg")#결과 이미지인 photo2를 jpg로 변환
    savePhoto.save(filename = saveFp.name)#파일 저장 대화창에서 입력받은 파일 이름으로 저장

def func_exit() :
    window.quit()
    window.destroy()
def func_zoomin() :
    global window,canvas,paper,photo,photo2,oriX,oriY
    if photo2 == None :
        return
    #askinteger() 함수를 실행해 대화 상자로 확대할 배수 입력받음
    scale = askinteger("확대배수", "확대할 배수를 입력하세요", minvalue = 2, maxvalue = 4)
    photo2.resize(int (oriX * scale), int (oriY * scale))#원본 이미지의 가로 세로 사이즈에 배수를 곱하여 크기 변경
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)#화면에 이미지를 출력하는 displayImage()함수 호출
def func_zoomout() :
    global window,canvas,paper,photo,photo2,oriX,oriY
    if photo2 == None :
        return
    scale = askinteger("축소", "축소할 배수를 입력하세요", minvalue = 2, maxvalue = 4)
    photo2.resize(int(oriX / scale), int(oriY / scale))#원본 이미지의 가로 세로 사이즈를 나눠서 크기 변경
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)#화면에 이미지를 출력하는 displayImage()함수 호출
def func_mirror1() :
    global window,canvas,paper,photo,photo2,oriX,oriY
    if photo2 == None :
        return
    photo2.flip()
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)
def func_mirror2() :
    global window,canvas,paper,photo,photo2,oriX,oriY
    if photo2 == None :
        return
    photo2.flop()
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)
def func_rotate() :
    global window,canvas,paper,photo,photo2,oriX,oriY
    if photo2 == None :
        return
    degree = askinteger("회전", "회전할 각도를 입력하세요", minvalue = 0, maxvalue = 360)
    photo2.rotate(degree)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)
def func_bright() :
    global window,canvas,paper,photo,photo2,oriX,oriY
    if photo2 == None :
        return
    value = askinteger("밝게", "값을 입력하세요(100~200)", minvalue = 100, maxvalue = 200)
    photo2.modulate(value, 100, 100)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)
def func_dark() :
    global window,canvas,paper,photo,photo2,oriX,oriY
    if photo2 == None :
        return
    value = askinteger("어둡게", "값을 입력하세요(0~100)", minvalue = 0, maxvalue = 100)
    photo2.modulate(value, 100, 100)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)
def func_clear() :
    global window,canvas,paper,photo,photo2,oriX,oriY
    if photo2 == None :
        return
    value = askinteger("선명하게", " 값을 입력하세요(100~200)", minvalue = 100, maxvalue = 200)
    photo2.modulate(100, value, 100)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)
def func_unclear() :
    global window,canvas,paper,photo,photo2,oriX,oriY
    if photo2 == None :
        return
    value = askinteger("탁하게", " 값을 입력하세요(0~100)", minvalue = 0, maxvalue = 100)
    photo2.modulate(100, value, 100)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)
#이미지 처리2 > 흑백이미지
#이미지의 type 값을 "grayscale"로 설정
def func_bw() :
    global window,canvas,paper,photo,photo2,oriX,oriY
    if photo2 == None :
        return
    photo2.type = "grayscale"
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)


#메인 코드 부분
window = Tk()
window.geometry("250x250")
window.title("미니 포토샵(Ver 0.1)")


#메뉴 생성
#1.메뉴 자체 생성 및 화면에 디스플레이
#메뉴 자체 이름 = Menu(부모 윈도우)
#부모 윈도우.config(munu=메뉴 자체 이름)
mainMenu = Menu(window)
window.config(menu = mainMenu)

#2.상위 메뉴 생성
#상위 메뉴 이름 = Menu(메뉴자체이름)
#메뉴자체이름.add_cascade(label = "상위 메뉴 텍스트" menu = 상위 메뉴 이름)
#add_cascade() 메소드는 메뉴자체와 상위 메뉴를 연결

fileMenu = Menu(mainMenu,tearoff=0)
mainMenu.add_cascade(label = "file", menu = fileMenu)
photo = PhotoImage()
pLabel = Label(window, image = photo)
pLabel.pack( expand = 1, anchor = CENTER)
#3. 하위 메뉴 생성
#상위메뉴 이름.add_command(label="하위 메뉴 이름",command = 함수명)
#add_command()메소드는 하위 메뉴 항목 생성
fileMenu.add_command(label = "file open",command = func_open)
fileMenu.add_command(label = "file save",command = func_save)
fileMenu.add_separator()
fileMenu.add_command(label = "window close",command = func_exit)

image1Menu = Menu(mainMenu,tearoff=0)
mainMenu.add_cascade(label = "이미지 처리(1)",menu = image1Menu)
image1Menu.add_command(label = "확대",command = func_zoomin)
image1Menu.add_command(label = "축소",command = func_zoomout)
image1Menu.add_separator()
image1Menu.add_command(label = "상하 반전",command = func_mirror1)
image1Menu.add_command(label = "좌우 반전",command = func_mirror2)
image1Menu.add_command(label = "회전",command = func_rotate)

image2Menu = Menu(mainMenu,tearoff=0)
mainMenu.add_cascade(label = "이미지 처리(2)",menu = image2Menu)
image2Menu.add_command(label = "밝게",command = func_bright)
image2Menu.add_command(label = "어둡게",command = func_dark)
image2Menu.add_separator()
image2Menu.add_command(label = "선명하게",command = func_clear)
image2Menu.add_command(label = "탁하게",command = func_unclear)
image2Menu.add_separator()
image2Menu.add_command(label = "흑백이미지",command = func_bw)

window.mainloop()


#원본으로 돌릴 수 있도록 메뉴 추가하고 함수도 추가
#채도와 색상도 조정가능하도록 응용
#나머지 UI 및 기능을 이미지 편집 프로그램 답게 커스터마이징 하기
#이미지를 불렀을때 파일명 표시