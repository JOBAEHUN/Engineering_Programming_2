"""
Created on Mon Mar 24 10:10:16 2025

@author: BaeHun
"""

inFp = None
inList = ""

inFp = open("C:/Temp/data1.txt", "r", encoding="utf-8")

inList = inFp.readlines()
print(inList)

inFp.close()