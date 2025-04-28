from tkinter import *
from tkinter.filedialog import *

# 전역 객체 미리 선언
photo = None
pLabel = None

def func_open():
    global photo, pLabel
    filename = askopenfilename(parent=window,
                                filetypes=(("GIF 파일", "*.gif"), ("모든 파일", "*.*")))
    if filename:
        photo = PhotoImage(file=filename)
        pLabel.configure(image=photo)
        pLabel.image = photo  # 반드시 유지시켜야 함

def func_exit():
    window.quit()
    window.destroy()

# 메인 창 설정
window = Tk()
window.geometry("500x500")
window.title("명화 감상하기")

# [수정 포인트] 처음에는 image 없이 Label을 만든다!
pLabel = Label(window)
pLabel.pack(expand=1, anchor=CENTER)

# 메뉴 생성
mainMenu = Menu(window)
window.config(menu=mainMenu)
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label="파일", menu=fileMenu)
fileMenu.add_command(label="파일 열기", command=func_open)
fileMenu.add_separator()
fileMenu.add_command(label="프로그램 종료", command=func_exit)

window.mainloop()
