"""
Created on Thu Apr 17 13:56:06 2025

@author: BaeHun
"""

import numpy as np

# 1. 배열 크기를 랜덤 선택
SIZE = np.random.choice([8, 12, 16, 20])
print(f"전체 배열 크기: {SIZE}x{SIZE}")

# 2. 전체 배열 생성 (1부터 시작)
total_values = SIZE * SIZE
array = np.arange(1, total_values + 1).reshape(SIZE, SIZE)

print("\n원본 배열:")
print(array)

# 3. 중앙부터 절반 크기의 슬라이싱 영역 설정
half = SIZE // 2
startRow = half // 2
startCol = half // 2

# 4. 슬라이싱 수행 (복사본)
center_array = array[startRow:startRow+half, startCol:startCol+half].copy()

print(f"\n중앙 {half}x{half} 배열:")
print(center_array)
