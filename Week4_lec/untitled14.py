"""
Created on Mon Mar 24 10:01:41 2025

@author: BaeHun
"""

inFp = None # 입력 파일
inStr = "" # 읽어온 문자열

inFp = open("C:/Temp/data1.txt", "r", encoding = "utf-8")

inStr = inFp.readline()
print(inStr, end ="")

inStr = inFp.readline()
print(inStr, end ="")

inStr = inFp.readline()
print(inStr, end ="")

inFp.close()
