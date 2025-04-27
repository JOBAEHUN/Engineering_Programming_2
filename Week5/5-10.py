from tkinter import *
import csv

## 함수선언부분##
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

## 전역변수부분##
csvList= []
rowNum, colNum= 0, 0
workSheet= []

## 메인코드부분##
window = Tk()

with open("E:/MyPythonProject/Week5_lec/singer1.csv", "r") as inFp:
    csvReader= csv.reader(inFp)
    header_list= next(csvReader)
    csvList.append(header_list)
    for row_list in csvReader:
        csvList.append(row_list)
    rowNum = len(csvList)
    colNum = len(csvList[0])
    workSheet = makeEmptySheet(rowNum, colNum)

idx = 6
for i in range(0, rowNum) :
    for k in range(0, colNum) :
        if ( csvList[i][idx].isnumeric() ) :
            if ( int(csvList[i][idx]) >= 167) :
                ent = workSheet[i][k]
                ent.configure(bg='yellow')
        workSheet[i][k].insert(0, csvList[i][k])
window.mainloop()