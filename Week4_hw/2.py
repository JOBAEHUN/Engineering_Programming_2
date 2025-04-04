"""
Created on Thu Mar 27 15:06:25 2025

@author: BaeHun
"""

from tkinter import *
from tkinter.filedialog import *
 ## 함수선언부분##
def func_open():
    global photo # global 변수로 선언
    filename = askopenfilename(parent = window, filetypes = (("GIF 파일", "*.gif"), ("모든파일", "*.*")))
    photo = PhotoImage(file = filename) # 이미지 파일 로드
    pLabel.configure(image = photo) # 라벨에 이미지 표시
    pLabel.image = photo # 참조 유지
    for y in range(photo.height()):
        for x in range(photo.width()):
            r, g, b = photo.get(x, y) # 픽셀 색상 추출
            gray = (r + g + b) // 3 # gray 값 계산
            photo.put("#%02x%02x%02x" % (gray, gray, gray), (x, y))
def func_exit():
    window.quit()
    window.destroy()

 ## 저장할 파일 경로 선택 ##
def func_save():
    saveFp=asksaveasfilename(parent=window,defaultextension='.raw', filetypes=(('RAW 파일', '*.raw'), ('모든 파일', '*.*')))
    if saveFp == '' or photo.width() == 0:
        return # 파일 선택 안하면 종료
    f = open(saveFp,'wb')
    for y in range(photo.height()):
        for x in range(photo.width()):
            r , g, b = photo.get(x,y)
            gray = r
            f.write(bytes([gray])) # 바이트로 변환 후 저장
    f.close()
## 메인코드부분##
window = Tk()

window.geometry("500x500")
window.title("명화감상하기")
photo = PhotoImage()
pLabel = Label(window, image = photo)
pLabel.pack(expand = 1, anchor = CENTER)
mainMenu = Menu(window)
window.config(menu = mainMenu)
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label = "파일", menu = fileMenu)
fileMenu.add_command(label = "파일열기", command = func_open)
fileMenu.add_command(label = "파일저장", command = func_save)
fileMenu.add_separator()
fileMenu.add_command(label = "프로그램종료", command = func_exit)
window.mainloop()