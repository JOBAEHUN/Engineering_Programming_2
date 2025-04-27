"""
Created on Sat Apr 26 16:13:12 2025

@author: BaeHun
"""

from tkinter import *
window = Tk()

btnList = [None] *3

for i in range(0,3):
    btnList[i] = Button(window, text = "버튼" + str(i + 1))
    
for btn in btnList :
    btn.pack(side = TOP) # TOP, BOTTOM, LEFT, RIGHT 모두 가능
    
window.mainloop()