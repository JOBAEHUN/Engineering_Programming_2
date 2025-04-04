"""
Created on Mon Mar 31 09:03:59 2025

@author: BaeHun
"""

def printList(pList):
    for data in pList:
        print(data, end='\t')
    print()
    
with open("C:/Temp/LED_wafer_Processing_summary.csv","r") as inFp:
    header = inFp.readline()
    header = header.strip()
    header_list = header.split(',')
    printList(header_list)
    for inStr in inFp:
        inStr = inStr.strip()
        row_list = inStr.split(',')
        printList(row_list)
        
