from tkinter import *
from tkinter.filedialog import *
 ## 함수선언부분##
def func_open() :
    filename = askopenfilename(parent = window, filetypes = (("GIF 파일", "*.gif"), ("모든파일", "*.*")))
    photo = PhotoImage(file = filename)
    pLabel.configure(image = photo)
    pLabel.image = photo
    # 이미지 전체를 회색으로 변환 #
    for y in range(photo.height()):
        for x in range(photo.width()):
            r, g, b = photo.get(x, y)
            gray = (r + g + b) // 3
            photo.put("#%02x%02x%02x" % (gray, gray, gray), (x, y))
def func_exit() :
    window.quit()
    window.destroy()
## 메인코드부분##
window = Tk()

window.geometry("500x500") # 창 크기 설정
window.title("명화감상하기")
photo = PhotoImage()
pLabel = Label(window, image = photo)
pLabel.pack(expand = 1, anchor = CENTER)
mainMenu = Menu(window)
window.config(menu = mainMenu)
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label = "파일", menu = fileMenu)
fileMenu.add_command(label = "파일열기", command = func_open)
fileMenu.add_separator()
fileMenu.add_command(label = "프로그램종료", command = func_exit)
window.mainloop()