aa = []
i = 0

# 1. 숫자 10개 입력받기
while i < 10:
    num = int(input(f"{i + 1}번째 숫자 : "))
    aa.append(num)
    i += 1

# 2. 합계 구하기 (while 사용)
hap = 0
i = 0
while i < 10:
    hap += aa[i]
    i += 1

# 3. 결과 출력
print("합계 ==> %d" % hap)
