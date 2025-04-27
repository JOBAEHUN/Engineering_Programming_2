inFp = None 
inStr = ""  
lineNo = 1  # 줄 번호 변수 추가

inFp = open("E:/MyPythonProject/Week4_lec/data1.txt", "r", encoding="utf-8")
while True:
    inStr = inFp.readline()
    if inStr == "":
        break
    print("%d : %s" % (lineNo, inStr), end="")  # 줄 번호와 내용 출력
    lineNo += 1  # 줄 번호 증가
inFp.close()
