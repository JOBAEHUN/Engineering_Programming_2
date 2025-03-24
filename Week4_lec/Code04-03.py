"""
Created on Mon Mar 24 09:06:50 2025

@author: BaeHun
"""

from tkinter import *
window = Tk()

label1 = Label(window, text = "파이썬을 이용한 데이터 분석을")
label2 = Label(window, text = "열심히", font = ("궁서체", 30), fg = "blue")
label3 = Label(window, text = "공부 중입니다.", bg = "magenta", width = 20, height = 5, anchor = SE)

label1.pack();
label2.pack();
label3.pack();


window.mainloop()