from tkinter import *

## 변수 선언 부분 ##

window = None
canvas = None
paper = None

XSIZE, YSIZE = 256, 256

## 메인 코드 부분 ##
window =Tk()
canvas = Canvas(window, height = XSIZE, width = YSIZE)

canvas.pack()

paper = PhotoImage(width = XSIZE, height = YSIZE)
canvas.create_image((XSIZE / 2, YSIZE / 2), image =paper, state = "normal")

window.mainloop()