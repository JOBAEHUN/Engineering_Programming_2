inFp = None
inList = ""

inFp = open("E:/MyPythonProject/Week4_lec/data1.txt", "r", encoding="utf-8")

inList = inFp.readlines()
print(inList)

inFp.close()