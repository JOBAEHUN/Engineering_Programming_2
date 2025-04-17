"""
Created on Mon Apr 14 09:10:22 2025

@author: BaeHun
"""

import random
 ## 파이썬2차원리스트생성
SIZE = 5
pythonList= [ [random.randint(0,255) for _ in range(SIZE)] for _ in range(SIZE)]
 ## 리스트를출력하기
for i in range(SIZE) :
 for k in range(SIZE) :
     print("%3d" % pythonList[i][k], end=' ')
 print()
print()
 ## 리스트에100을더하기
for i in range(SIZE) :
 for k in range(SIZE) :
     pythonList[i][k] += 100
 ## 리스트를출력하기
for i in range(SIZE) :
    for k in range(SIZE) :
        print("%3d" % pythonList[i][k], end=' ')
    print()
