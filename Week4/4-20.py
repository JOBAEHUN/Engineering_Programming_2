inFp = None
inList, inStr = [], ""

inFp = open("E:/MyPythonProject/Week4_lec/data1.txt", "r", encoding="utf-8")

inList = inFp.readlines()
for inStr in inList:
    print(inStr, end = "")
    
inFp.close()