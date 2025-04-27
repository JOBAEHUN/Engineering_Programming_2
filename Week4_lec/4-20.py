"""
Created on Mon Mar 24 10:11:37 2025

@author: BaeHun
"""

inFp = None
inList, inStr = [], ""

inFp = open("E:/MyPythonProject/Week4_lec/data1.txt", "r", encoding="utf-8")

inList = inFp.readlines()
for inStr in inList:
    print(inStr, end = "")
    
inFp.close()