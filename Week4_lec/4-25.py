from tkinter import *

## 전역 변수 선언 부분 ##
window, canvas, paper = None, None, None
XSIZE, YSIZE = 256, 256
inImage = []

## 함수 선언 부분 ##
def loadImage(fname):
    global inImage, XSIZE, YSIZE
    fp = open(fname, 'rb')
    for i in range(XSIZE):
        tmpList = []
        for k in range(YSIZE):
            data = int(ord(fp.read(1)))
            tmpList.append(data)
        inImage.append(tmpList)
    fp.close()

def displayImage(image):
    global paper
    for i in range(XSIZE):
        for k in range(YSIZE):
            gray = image[i][k]
            paper.put("#%02x%02x%02x" % (gray, gray, gray), (k, i))

## 메인 코드 ##
window = Tk()
window.title("흑백 사진 보기")
canvas = Canvas(window, height=XSIZE, width=YSIZE)
paper = PhotoImage(width=XSIZE, height=YSIZE)
canvas.create_image((XSIZE / 2, YSIZE / 2), image=paper, state="normal")

filename = 'tree.raw'
loadImage(filename)
displayImage(inImage)

canvas.pack()
window.mainloop()
