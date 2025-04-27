inFp = None
inList, inStr = [], ""
lineNum =1

inFp = open("E:/MyPythonProject/Week4_lec/data1.txt", "r", encoding="utf-8")


inList = inFp.readlines()
for inStr in inList:
    print("%d : %s" %(lineNum,inStr), end = "")
    lineNum += 1
inFp.close()