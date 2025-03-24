"""
Created on Mon Mar 24 10:22:20 2025

@author: BaeHun
"""

from tkinter import *

## 변수 선언부분##
window = None
canvas = None
XSIZE, YSIZE = 256, 256

## 메인 코드부분##
window = Tk()
canvas = Canvas(window, height = XSIZE, width = YSIZE)
paper = PhotoImage(width = XSIZE, height = YSIZE)
canvas.create_image((XSIZE / 2, YSIZE / 2), image = paper, state ="normal")


canvas.pack()
window.mainloop()