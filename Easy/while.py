aa = []
hap = 0
i=0
while i < 10:
     i = i + 1
     aa.append(0)
     aa[i - 1] = int(input(str(i) + "번째 숫자: "))
     
hap = aa[0] + aa[1] + aa[2] + aa[3] + aa[4] + aa[5] + aa[6] + aa[7] + aa[8] + aa[9]  # 모든 값 더하기
print("합계==> %d" % hap)