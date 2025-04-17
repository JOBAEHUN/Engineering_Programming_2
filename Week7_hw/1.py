"""
Created on Thu Apr 17 13:50:28 2025

@author: BaeHun
"""

import numpy as np

# 3x3 배열 생성 (0~99 사이의 랜덤 정수)
array = np.random.randint(0, 100, size=(3, 3))

print("원본 배열:")
print(array)

# 배열 값 2배로 증가
array *= 2

print("\n2배 증가된 배열:")
print(array)

# 파이썬 for문으로 평균값 계산
total = 0
count = 0

for row in array:
    for val in row:
        total += val
        count += 1

average = total / count
print("\n평균값:", average)
