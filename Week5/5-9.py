from tkinter import *

# 함수 선언 부분
def makeEmptySheet(r,w) :
    retList =[]
    for i in range(0,r):
        tmpList = []
        for k in range(0,w):
            ent = Entry(window, text ="", width =10)
            ent.grid(row = i, column = k)
            tmpList.append(ent)
        retList.append(tmpList)
    return retList
# 전역 변수 부분
csvList = [['제목1','제목2','제목3'],
           [111, 222, 333],
           [444, 555, 666],
           [777, 888, 999]]

rowNum, colNum = 4,3
workSheet =[]

#메인 코드 부분
window =Tk()
workSheet = makeEmptySheet(rowNum, colNum)

for i in range(0,rowNum):
    for k in range(0,colNum):
        workSheet[i][k].insert(0, csvList[i][k])
        
window.mainloop()