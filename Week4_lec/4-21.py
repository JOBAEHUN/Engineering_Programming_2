outFp = None
outSrt =""

outFp = open("E:/MypythonProject/Week4_lec/data2.txt","w")

while True:
    outStr = input("내용 입력: ")
    if outStr != "":
        outFp.writelines(outStr + "\n")
    else:
        break
    
outFp.close()
print("--- 정상적으로 파일에 씀 ---")