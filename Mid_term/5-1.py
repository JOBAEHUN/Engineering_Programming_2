inFp = open("E:/MyPythonProject/Week5_lec/LED_wafer_Processing_summary.csv", "r")

inStr = inFp.readline()
print(inStr,end =" ")

inStr = inFp.readline()
print(inStr, end =" ")

inFp.close()