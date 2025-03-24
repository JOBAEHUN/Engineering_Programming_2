"""
Created on Mon Mar 24 10:17:47 2025

@author: BaeHun
"""

inFp, outFp = None, None 
inStr = ""
inFp = open("C:/Windows/win.ini", "r")
outFp = open("C:/Temp/data3.txt", "w")
inList = inFp.readlines()
for inStr in inList :
    outFp.writelines(inStr)

inFp.close()
outFp.close()
print("--- 파일이 정상적으로 복사되었음---")