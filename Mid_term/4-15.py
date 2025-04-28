from tkinter import *
from tkinter.filedialog import *
 
## 함수선언부분##
window = Tk()
window.geometry("400x100")
label1 = Label(window, text = "선택된파일이름")
label1.pack()
saveFp = asksaveasfile(parent = window, mode = "w", defaultextension = ".jpg", \
         filetypes = (("JPG 파일", "*.jpg;*.jpeg"), ("모든파일", "*.*")))
label1.configure(text = saveFp)
saveFp.close()
