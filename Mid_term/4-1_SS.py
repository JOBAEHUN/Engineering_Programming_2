from tkinter import *
window= Tk()
window.title("고양이")

photo1 = PhotoImage(file="cat3.gif")
label1 = Label(window, image=photo1)

photo2 = PhotoImage(file="cat4.gif")
label2 = Label(window, image=photo2)

label1.pack(side=LEFT)
label2.pack(side=LEFT)

window.mainloop()