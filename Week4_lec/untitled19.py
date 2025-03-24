"""
Created on Mon Mar 24 10:19:56 2025

@author: BaeHun
"""

inFp, outFp = None, None 
inStr = ""

inFp = open("C:/Windows/write.exe", "rb")
outFp = open("C:/Temp/write.exe", "wb")

while True :
    inStr = inFp.read(1)
    if not inStr :
        break
    outFp.write(inStr)
inFp.close()
outFp.close()
print("--- 이진 파일이정상적으로복사되었음---")