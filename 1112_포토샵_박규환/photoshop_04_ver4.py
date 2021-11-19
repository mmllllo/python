# 미니 포토샵 수정본 (배경 추가, 메뉴 수정)
# 포토샵과 같은 소프트웨어를 '영상처리(Image Processing) 프로그램'이라 함
# 원칙적으로 영상처리에 대한 이론과 알고리즘을 익힌 후 미니 포토샵 프로그램을 작성하면 좋음
# 현실적으로 이론은 배제하고 화면에 구현되는 것 위주로 진행

# 주의 사항1.이미지 파일명이나 저장된 경로에 한글이 들어가면 안됨
# 주의 사항2. 이미지 크기는 가로와 세로가 동일해야 함
# 주의 사항3. 처리하는 속도가 다소 오래 걸림

# [수정사항]
# 1. 각 메뉴에 대해서 원본을 복제한 이미지가 아닌 직전 이미지에 함수를 적용하도록 수정
# 2. 윈도우 사이즈 고정, 캔버스 중간 배치
# 3. Wand의 다양한 함수 적용 (참고, https://yoonkh.github.io/python/2017/12/10/brain6.html)
# 3-1. modulate(명도값, 채도값, 색상값)으로 색상을 변경하는 메뉴와 함수를 추가
# 3-2. composite(),transparentize(),watermark()함수를 활용하여 두개의 이미지 합성

# 사용할 라이브러리 또는 모듈을 임포트
from tkinter import *
from tkinter.filedialog import *
from tkinter.simpledialog import *
# 설치한 이미지 처리 기능을 제공하는 이미지매직의 라이브러리 임포트
# GIF 뿐 아니라 JPG, PNG 같은 이미지를 모두 처리하기 위해 외부 라이브러리 이미지 매직 사용 
from wand.image import * 

# 모든 함수들이  공통적으로 사용할 전역 변수 선언부
window,canvas, paper=None, None, None
photo, photo2=None, None #photo는 처음 불러들인 원본 이미지, photo2는 처리 결과를 저장할 변수
oriX,oriY,newX, newY= 0,0,0,0 # 원본 이미지의 폭과 높이를 저장하는 함수


# 함수 정의부, 각 메뉴를 선택할 때 실행될 함수 선언

# displayImage(이미지, 가로사이즈, 세로사이즈) 함수는 메뉴를 선택할 때마다 실행되는 것이 아니라,
# 이미지를 화면에 출력하는 함수
# 각 함수에서 처리한 결과 이미지의 세가지 정보를 넘겨받아 이미지를 가로와 세로 사이즈대로 화면에 출력

# [displayImage() 함수의 처리 과정]
# 1.넘겨받은 이미지의 크기와 동일하게 윈도우 창의 크기 설정
# 2.새 캔버스 생성, 기존에 이미지가 출력된 캔버스를 깨끗하게 처리
# 3.새 캔버스에 종이(paper)를 붙인 후 처리된 이미지를 그 위에 출력
# 4.흰종이에 사진을 출력하기 위해 이미지 파일의 모든 점(픽셀)에 접근
# 5.이미지의 폭과 높이만큼 반복해서 픽셀의 RGB 값을 추출하고
# 6.paper에 이미지의 픽셀을 칼라로 찍어 이미지 구현
# 7.처리된 결과 이미지의 픽셀을 찍어둔 종이paper가 붙여있는 캔버스를 화면에 출력

def displayImage(img, width, height) :
    global window,canvas, paper, photo, photo2, oriX, oriY, newX, newY, last_index  # 전역 변수 선언

    # 넘겨받은 이미지의 크기와 동일하게 윈도우 창의 크기를  설정
    # window.geometry(str(width)+"x"+str(height))
    # 이전 캔버스가 존배한다면 새 캔버스와 그 위에 새 종이를 생성하여 깨끗하게 처리한 후 처리된 이미지 출력
    # 이전 캔버스가 존재한다면 이전 캔버스를 삭제하여 기존에 이미지가 출력된 캔버스를 깨끗하게 처리
    if canvas != None :
        canvas.destroy()
    # 새 캔버스 생성, 처리된 이미지의 가로 세로 사이즈대로 생성
    # 캔버스의 흰색 테두리 없애기, bd=0, highlightthickness=0
    canvas = Canvas(window, width=width, height=height, bd=0, highlightthickness=0)
    # 새 캔버스에 붙일 종이(paper) 생성, 처리된 이미지의 가로 세로 사이즈대로 생성 
    # 새 종이는 다양한 이미지 파일 포맷이 아닌 단순히 빈 이미지를 보여줄 것이라 PhotoImage()로 생성
    paper=PhotoImage(width=width, height=height)
    # 기존 make_blob(format='RGB')는 픽셀을 일일이 이미지의 가로, 세로 사이즈만큼 페이퍼에 찍어서 표현하기 때문에
    # 처리 시간이 많이 걸림
    # img.make_blob(format='png') 방식으로 처리할 경우 이미지 처리 시간이 빨라짐, 투명한 배경 지원
    blob = img.make_blob(format='png')
    paper.put(blob) 
    # 새 캔버스에 종이(paper)를 붙임 ( 차후 그 종이 위에 처리된 이미지를 출력)
    # 생성될 위치는 가로 세로의 사이즈의 중간 위치
    
    canvas.create_image( (width/2, height/2), image=paper, state="normal")


    # 새 캔버스와 새 종이 위에 처리된 이미지를 출력
    # func_open()에서 이미지를 불러오면  Wand 라이브러리의 Image()를 사용헤서 이미지 생성
    # Image()에 의해 생성된 이미지는 configure()함수를 적용할 수 없기 때문에 아래 방식으로 이미지를 표현
    '''
    # 흰종이에 사진을 출력하기 위해 이미지 파일의 모든 점(픽셀)에 접근
    blob = img.make_blob(format='RGB')
    # 이미지의 폭과 높이만큼 반복해서 픽셀의 RGB 값을 추출
    for i in range(0, width) :
        for k in range(0, height) :
            r = blob[(i*3*width)+(k*3) + 0]
            g = blob[(i*3*width)+(k*3) + 1]
            b = blob[(i*3*width)+(k*3) + 2]
            # paper에 칼라로 점을 찍어줌
            paper.put("#%02x%02x%02x" % (r,g,b) , (k, i))
    # 처리된 결과 이미지의 픽셀을 찍어둔 종이paper가 붙여있는 캔버스를 화면에 출력
    '''
    canvas.place(x=(780-width)/2, y=(620-height)/2+15)
    #canvas.pack(expand=1, anchor=CENTER) # 중앙 정렬

def displayImage2(img, width, height) :
    global window,canvas, paper, photo, photo2, oriX, oriY, newX, newY  # 전역 변수 선언

    if canvas != None :
        canvas.destroy()

    canvas = Canvas(window, width=width, height=height, bd=0, highlightthickness=0)

    paper=PhotoImage(width=width, height=height)
    
    blob = img.make_blob(format='png')
    paper.put(blob) 
    canvas.create_image( (width/2, height/2), image=paper, state="normal")

    canvas.place(x=(780-width)/2, y=(620-height)/2+15)

    
# 파일 열기
def func_open() :
    global window,canvas, paper, photo, photo2, oriX, oriY, newX, newY  # 전역 변수 선언
    # askopenfilename() 함수로 파일 열기 대화상자를 나타내어 그림 파일 선택
    readFp = askopenfilename(parent=window, filetypes=(("모든 그림 파일", "*.jpg;*.jpeg;*.bmp;*.png;*.tif;*.gif"),  ("모든 파일", "*.*") ))

    # [파열 열기] 메뉴를 통해 선택된 원본 이미지는 photo에 저장
    # 함수에 의해 처리되어 화면에 보여질 이미지는 photo2에 저장

    # 미니 포토샵은 다음 함수를 실행할 때마다
    # 직전 이미지 photo2의 정보가 아닌 원본 이미지 photo의 정보에 대해 명령을 적용하는 원리
    # 함수를 거듭 실행하면 원본 이미지가 훼손되기 때문
    # 다음 함수를 실행하면 화면에서 photo2는 매번 원본 photo를 복제하여 명령 처리
    # 만약 함수를 실행할 때 직전 이미지에 적용하기 위해서는 복제 과정을 생략하면 됨

    # 이미지는 GIF, JPG, PNG를 불러와 모두 처리하기 위해 PhotoImage() 가 아닌
    # Wand 라이브러리에서 제공하는 Image() 객체를 사용

    # photo는 처음 불러들인 원본 이미지
    photo = Image(filename=readFp) 
    oriX = photo.width  # 원본 이미지의 가로 사이즈를 oriX에 저장
    oriY = photo.height # 원본 이미지의 세로 사이즈를 oriX에 저장

    # 닫기 버튼 출력하기
    btn_close = Button(window, text="X", command=func_close)
    btn_close.place(x=45, y=32)
    
    # 화면에 파일 이름 출력하기
    string = readFp
    p =string.split('/')
    s = len(p)
    photo_Label.configure(text=str(p[s-1]))

    #photo2는 처리 결과를 저장할 변수
    photo2 = photo.clone()  # 원본 이미지의 photo를 복사하여 photo2에 저장
    newX = photo2.width 
    newY = photo2.height
    displayImage(photo2, newX, newY)

    # 비활성화 메뉴 활성화
    fileMenu.entryconfigure("Save As", state=NORMAL)
    fileMenu.entryconfigure("Revert", state=NORMAL)
    image1Menu.entryconfigure("Rotate", state=NORMAL)
    image1Menu.entryconfigure("Flip Horizontal", state=NORMAL)
    image1Menu.entryconfigure("Flip Vertical", state=NORMAL)
    image2Menu.entryconfigure("Hue", state=NORMAL)
    image2Menu.entryconfigure("Brightness", state=NORMAL)
    image2Menu.entryconfigure("Saturation", state=NORMAL)
    image3Menu.entryconfigure("Composite", state=NORMAL)
    image3Menu.entryconfigure("Sepia", state=NORMAL)
    image3Menu.entryconfigure("Shade", state=NORMAL)
    image3Menu.entryconfigure("Sketch", state=NORMAL)
    image4Menu.entryconfigure("Zoom In", state=NORMAL)
    image4Menu.entryconfigure("Zoom Out", state=NORMAL)



# 파일 저장
def func_save() :
    global window,canvas, paper, photo, photo2, oriX, oriY, newX, newY  # 전역 변수 선언

    # photo2는 파일을 열면 생성됨, 파일을 열지 않았다면 저장하기를 눌렀을 때 함수를 빠져나감
    if photo2 == None :
        return
    #saveFp = asksaveasfile(parent=window, mode="w", defaultextension=".jpg", filetypes=(("JPG 파일", "*.jpg;*.jpeg"),  ("모든 파일", "*.*") ))
    #savePhoto = photo2.convert("jpg") # 결과 이미지인 photo2를 jpg로 변환
    saveFp = asksaveasfile(parent=window, mode="w", defaultextension=".png", filetypes=(("PNG file", "*.png"),  ("A;;", "*.*") ))
    savePhoto = photo2.convert("png") # 결과 이미지인 photo2를png 방식으로 변환
    savePhoto.save(filename=saveFp.name) # 파일 저장 대화창에서 입력받은 파일 이름으로 저장

# 캔버스 닫기
def func_close() :
    canvas.destroy()
    photo_Label.configure(text="")
    
# 프로그램 저장
def func_exit() :
    window.quit()
    window.destroy()

# 이미지 처리1 > 확대 및 축소
# 대화창을 통해 정수를 입력받아 그 수만큼 이미지를 확대하거나 축소함
# Wand 라이브러리에서 제공하는 resize(가로,세로)함수를 사용
# 너무 큰 수자를 입력하면 처리하는데 시간이 걸리므로 숫자를 2~4로 제한

# 확대, 확대할 배수를 입력받아 그 배수만큼 이미지의 크기를 확대함
def func_zoomin() :
    global window,canvas, paper, photo, photo2, oriX, oriY, newX, newY, last_index  # 전역 변수 선언
    # 파일을 열지 않았다면 명령어를 실행했을 때 함수를 빠져나감
    if photo2 == None :
        return
    # askinteger() 함수를 실행해 대화 상자로 확대할 배수 입력받음
    scale = askinteger("확대배수", "확대할 배수를 입력하세요(2~4)", minvalue=2, maxvalue=4) # 대화 상자로 확대할 배수 입력받음
    # 만약 함수를 실행할 때 직전 이미지에 적용하기 위해서는 복제 과정을 생략하면 됨
    #photo2 = photo.clone()  # 원본 이미지 photo를 복제하여 photo2에 저장
    photo2.resize( int(newX * scale) , int(newY * scale) ) # 원본 이미지의 가로 세로 사이즈에 배수를 곱하여 크기 변경
    newX = photo2.width # 변경된 이미지의 가로 사이즈 newX에 저장
    newY = photo2.height  # 변경된 이미지의 세로 사이즈 newY에 저장  
    displayImage(photo2, newX, newY) # 처리된 이미지의 이미지, 가로,세로 정보를 displayImage() 함수에 넘겨줌

# 축소, 축소할 배수를 입력받아 그 배수만큼 이미지의 크기를 축소함
def func_zoomout() :
    global window,canvas, paper, photo, photo2, oriX, oriY, newX, newY  # 전역 변수 선언
    scale = askinteger("축소", "축소할 배수를 입력하세요(2~4)", minvalue=2, maxvalue=4)
    #photo2 = photo.clone()  # 원본 이미지 photo를 복제하여 photo2에 저장
    photo2.resize( int(newX / scale) , int(newY / scale) ) # 원본 이미지의 가로 세로 사이즈에 배수를 나누어 크기 변경
    newX = photo2.width 
    newY = photo2.height    
    displayImage(photo2, newX, newY)

# 이미지 처리1 > 상하/좌우 반전
# Wand 라이브러리에서 제공하는 flip()함수와 flop()함수를 사용

# 상하 반전, flip()
def func_mirror1() :
    global window,canvas, paper, photo, photo2, oriX, oriY, newX, newY  # 전역 변수 선언
    #photo2 = photo.clone()
    photo2.flip()
    newX = photo2.width 
    newY = photo2.height
    displayImage(photo2, newX, newY)

# 좌우 반전, flop()
def func_mirror2() :
    global window,canvas, paper, photo, photo2, oriX, oriY, newX, newY  # 전역 변수 선언
    #photo2 = photo.clone()
    photo2.flop()
    newX = photo2.width 
    newY = photo2.height
    displayImage(photo2, newX, newY)

# 이미지 처리1 > 회전
# 대화창을 통해 정수를 입력받아 그 수만큼 회전
# Wand 라이브러리에서 제공하는 resize(가로,세로)함수를 사용

def func_rotate() :
    global window,canvas, paper, photo, photo2, oriX, oriY, newX, newY  # 전역 변수 선언
    degree = askinteger("회전", "회전할 각도를 입력하세요(0~360)", minvalue=0, maxvalue=360) 
    #photo2 = photo.clone()
    photo2.rotate(degree)
    newX = photo2.width 
    newY = photo2.height
    displayImage(photo2, newX, newY)

# 이미지 처리2 > 밝게 / 어둡게
# 대화창을 통해 정수를 입력받아 그 수만큼 이미지의 명도를 조정
# Wand 라이브러리에서 제공하는 modulate(명도값, 채도값, 색상값)함수를 사용

# 명도는 modulate(명도값, 100,100)함수를 사용
# 원본의 명도값이 100이므로 100 이상은 '밝게', 100 이하는 '어둡게' 처리

# 밝게, modulate(밝기값, 100,100)함수에 100~200 값 입력
def func_bright() :
    global window,canvas, paper, photo, photo2, oriX, oriY, newX, newY  # 전역 변수 선언
    value = askinteger("밝게", "값을 입력하세요(100~200)", minvalue=100, maxvalue=200)
    #photo2 = photo.clone()
    photo2.modulate(value, 100, 100)
    newX = photo2.width 
    newY = photo2.height
    displayImage(photo2, newX, newY)    

# 어둡게, modulate(밝기값, 100,100)함수에 0~100 값 입력
def func_dark() :
    global window,canvas, paper, photo, photo2, oriX, oriY, newX, newY  # 전역 변수 선언
    value = askinteger("어둡게", "값을 입력하세요(0~100)", minvalue=0, maxvalue=100)
    #photo2 = photo.clone()
    photo2.modulate(value, 100, 100)
    newX = photo2.width 
    newY = photo2.height
    displayImage(photo2, newX, newY)

# 이미지 처리2 > 선명하게/탁하게
# 대화창을 통해 정수를 입력받아 그 수만큼 이미지의 채도를 조정
# Wand 라이브러리에서 제공하는 modulate(100,채도값,100)함수를 사용
# 원본의 채도값이 100이므로 100 이상은 '선명하게', 100 이하는 '탁하게' 처리    

# 선명하게, modulate(100,채도값,100)함수에 100~200 값 입력
def func_clear() :
    global window,canvas, paper, photo, photo2, oriX, oriY, newX, newY  # 전역 변수 선언
    value = askinteger("선명하게", "값을 입력하세요(100~200)", minvalue=100, maxvalue=200)
    #photo2 = photo.clone()
    photo2.modulate(100, value, 100)
    newX = photo2.width 
    newY = photo2.height
    displayImage(photo2, newX, newY)

# 탁하게, modulate(100,채도값,100)함수에 0~100 값 입력
def func_unclear() :
    global window,canvas, paper, photo, photo2, oriX, oriY, newX, newY  # 전역 변수 선언
    value = askinteger("탁하게", "값을 입력하세요(0~100)", minvalue=0, maxvalue=100)
    #photo2 = photo.clone()
    photo2.modulate(100, value,100)
    newX = photo2.width 
    newY = photo2.height
    displayImage(photo2, newX, newY)

# 색상 변경, modulate(100,채도값,100)함수에 100~200 값 입력
def func_hue() :
    global window,canvas, paper, photo, photo2, oriX, oriY, newX, newY  # 전역 변수 선언
    value = askinteger("색상변경", "값을 입력하세요(0~200)", minvalue=0, maxvalue=200)
    #photo2 = photo.clone()
    photo2.modulate(100, 100,value)
    newX = photo2.width 
    newY = photo2.height
    displayImage(photo2, newX, newY)


# 이미지 처리2 > 흑백이미지
# 이미지의 type 값을 "grayscale"로 설정

def func_bw() :
    global window,canvas, paper, photo, photo2, oriX, oriY, newX, newY  # 전역 변수 선언
    #photo2 = photo.clone()
    photo2.type="grayscale"
    newX = photo2.width 
    newY = photo2.height
    displayImage(photo2, newX, newY)

# 이미지 처리2 > 이미지합성
# Image 객체의 composite(합성할 이미지,x좌표, y좌표) 함수로 두개의 이미지 합성
# photo2.composite(photo1, 20, 20) 는 photo2의 (20, 20) 위치에 photo1를 합성
# Image 객체의 transparentize(투명도) 함수로 한쪽 이미지를 투명하게 처리하여 합성하면 자연스러움
# transparentize() 메소드는 투명도를 0에서 1사이의 값으로 입력받음, 1은 100%, 0.7은 70%를 의미

# Image 클래스 watermark()함수는 composite() 함수와 transparentize() 함수의 기능을 한꺼번에 수행
# 대상이미지.watermark(합성할 이미지, 투명도, x좌표, y좌표)

def func_comp() :
    global window,canvas, paper, photo, photo2, oriX, oriY, newX, newY  # 전역 변수 선언
    #photo2 = photo.clone()
    '''
    photo.transparentize(0.5) # 원본 이미지의 투명도를 50%로 설정
    photo2.composite(photo, 20, 20) # photo2의 20, 20 위치에 photo를 합성
    '''
    photo2.watermark(photo, 0.5, 20, 20)
    newX = photo2.width 
    newY = photo2.height
    displayImage(photo2, newX, newY)

# 추가기능
# 되돌리기
def func_revert() :
    global window,canvas, paper, photo, photo2, oriX, oriY,newX, newY  # 전역 변수 선언
    # 파일을 열지 않았다면 명령어를 실행했을 때 함수를 빠져나감
    if photo2 == None :
        return

    photo2 = photo.clone() # 원본을 복제해서 photo2 덮어쓰기
    newX = photo2.width 
    newY = photo2.height
    displayImage(photo2, newX, newY)

# 이미지를 세피아톤으로 변화
def func_sepia() :
    global window,canvas, paper, photo, photo2, oriX, oriY,newX, newY  # 전역 변수 선언
    # 파일을 열지 않았다면 저장하기를 눌렀을 때 함수를 빠져나감
    if photo2 == None :
        return
    S_tone = askinteger("세피아 진하기", "세피아톤 진하기를 입력하세요(1~9)",minvalue=1, maxvalue=9)
    photo2=photo.clone()
    photo2.sepia_tone(threshold= S_tone/10.0)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)

# 이미지를 셰이더로 변화
def func_shade() :
    global window,canvas, paper, photo, photo2, oriX, oriY,newX, newY  # 전역 변수 선언
    # 파일을 열지 않았다면 저장하기를 눌렀을 때 함수를 빠져나감
    if photo2 == None :
        return
    Sh_Br = askinteger("세이드 밝기", "세이드의 밝기를 입력하세요(1~99)",minvalue=1, maxvalue=99)
    photo2=photo.clone()
    photo2.shade(gray=True, azimuth=286.0, elevation=Sh_Br)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)

# 이미지를 스케치로 변화
def func_sketch() :
    global window,canvas, paper, photo, photo2, oriX, oriY,newX, newY  # 전역 변수 선언
    # 파일을 열지 않았다면 저장하기를 눌렀을 때 함수를 빠져나감
    if photo2 == None :
        return
    photo2.transform_colorspace("gray")
    photo2.sketch(0.5, 0.0, 98.0)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)

# 이미지에 블러 효과 적용
def func_spread() :
    global window,canvas, paper, photo, photo2, oriX, oriY,newX, newY  # 전역 변수 선언
    # 파일을 열지 않았다면 저장하기를 눌렀을 때 함수를 빠져나감
    if photo2 == None :
        return
    blur = askinteger("블러의 선명도", "블러의 강도를 입력하세요(1~9)",minvalue=1, maxvalue=9)
    photo2=photo.clone()
    photo2.spread(radius=blur)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)


# 메인 코드부
window = Tk()
window.geometry("958x620")
window.title("Mini Photoshop (Ver 0.5) _ by SunnyLee")

# 배경 이미지 출력
bg_photo = PhotoImage(file = "bgimg.png")
pLabel = Label(window, image=bg_photo)
#pLabel.pack( expand=1, anchor=CENTER)
pLabel.place(x=-2, y=-2)

# 화면에 파일 이름 출력하기
photo_Label=Label(window, text="", fg="white",bg='#4f4f4f')
photo_Label.place(x=75, y=32)


# 메뉴 구현
# 메뉴 자체 생성
mainMenu = Menu(window)
window.config(menu=mainMenu)

# 상위 메뉴 생성
# tearoff=0, 상위 메뉴와 하위 메뉴 사이 점선 없애기
fileMenu = Menu(mainMenu, tearoff=0)
mainMenu.add_cascade(label="File", menu=fileMenu)
# 하위 메뉴 생성
fileMenu.add_command(label="Open...", command=func_open)
fileMenu.add_command(label="Save As", command=func_save, state=DISABLED)
fileMenu.add_separator() # 구분선 삽입
fileMenu.add_command(label="Revert", command=func_revert, state=DISABLED)
fileMenu.add_separator() # 구분선 삽입
fileMenu.add_command(label="Close", command=func_close)
fileMenu.add_command(label="Exit", command=func_exit)

image1Menu = Menu(mainMenu, tearoff=0)
mainMenu.add_cascade(label="Edit", menu=image1Menu)
image1Menu.add_command(label="Rotate", command=func_rotate, state=DISABLED)
image1Menu.add_separator() # 구분선 삽입
image1Menu.add_command(label="Flip Horizontal", command=func_mirror2, state=DISABLED)
image1Menu.add_command(label="Flip Vertical", command=func_mirror1, state=DISABLED)

image2Menu = Menu(mainMenu, tearoff=0)
image2Menu_01 = Menu(mainMenu, tearoff=0)
image2Menu_02 = Menu(mainMenu, tearoff=0)
image2Menu_03 = Menu(mainMenu, tearoff=0)
mainMenu.add_cascade(label="Image", menu=image2Menu)
image2Menu.add_cascade(label="Hue", menu=image2Menu_01, state=DISABLED)
image2Menu_01.add_command(label="Hue", command=func_hue)

image2Menu.add_cascade(label="Brightness", menu=image2Menu_02, state=DISABLED)
image2Menu_02.add_command(label="Brightness Up", command=func_bright)
image2Menu_02.add_command(label="Brightness Down", command=func_dark)

image2Menu.add_cascade(label="Saturation", menu=image2Menu_03, state=DISABLED)
image2Menu_03.add_command(label="Saturation Up", command=func_clear)
image2Menu_03.add_command(label="Saturation Down", command=func_unclear)
image2Menu_03.add_command(label="Desaturate", command=func_bw)


image3Menu = Menu(mainMenu, tearoff=0)
mainMenu.add_cascade(label="Filter", menu=image3Menu)
image3Menu.add_command(label="Composite", command=func_comp, state=DISABLED)
image3Menu.add_separator() # 구분선 삽입
image3Menu.add_command(label="Sepia", command=func_sepia, state=DISABLED)
image3Menu.add_command(label="Shade", command=func_shade, state=DISABLED)
image3Menu.add_command(label="Sketch", command=func_sketch, state=DISABLED)
image3Menu.add_command(label="Blur", command=func_spread, state=DISABLED)

image4Menu = Menu(mainMenu, tearoff=0)
mainMenu.add_cascade(label="View", menu=image4Menu)
image4Menu.add_command(label="Zoom In", command=func_zoomin, state=DISABLED)
image4Menu.add_command(label="Zoom Out", command=func_zoomout, state=DISABLED)

window.mainloop()
