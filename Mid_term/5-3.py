def printList(pList):
    for data in pList:
        print(data, end='\t')
    print()
    
with open("E:/MyPythonProject/Week5_lec/LED_wafer_Processing_summary.csv","r") as inFp:
    header = inFp.readline()
    header = header.strip()
    header_list = header.split(',')
    printList(header_list)
    for inStr in inFp:
        inStr = inStr.strip()
        row_list = inStr.split(',')
        printList(row_list)
        
