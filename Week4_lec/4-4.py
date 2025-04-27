"""
Created on Mon Mar 24 09:09:26 2025

@author: BaeHun
"""

from tkinter import*
window = Tk()

photo = PhotoImage(file="dog13.gif")
label1 = Label(window, image =photo)

label1.pack();

window.mainloop()
