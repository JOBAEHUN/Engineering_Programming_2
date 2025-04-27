"""
Created on Mon Mar 24 10:06:11 2025

@author: BaeHun
"""

inFp = None 
inStr = ""  

inFp = open("E:/MyPythonProject/Week4_lec/data1.txt", "r", encoding="utf-8" )
while True :
     inStr = inFp.readline()
     if inStr == "" :
         break;
     print(inStr, end = "")
inFp.close()