"""
Created on Fri Apr 25 14:33:08 2025

@author: BaeHun
"""

aa = []
for i in range(0,4):
    aa.append(0)
hap = 0

for i in range(0,4):
    aa[i] = int(input(str(i + 1) + "번째 숫자 :"))

hap = aa[0] + aa[1] + aa[2] + aa[3]

print("합계 ==> %d" % hap)
