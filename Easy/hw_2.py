import numpy as np

SIZE = np.random.choice([8, 12, 16, 20]) # 배열 크기를 랜덤 선택

total_values = SIZE * SIZE
array = np.arange(1, total_values + 1).reshape(SIZE, SIZE) # 1부터~ (SIZE,SIZE) 배열 생성

print(f"원본 {SIZE}x{SIZE} 배열:")
print(array)

half = SIZE // 2
startRow = half // 2
startCol = half // 2

center_array = array[startRow:startRow+half, startCol:startCol+half].copy() #슬라이싱 후 복사

print(f"\n중앙 {half}x{half} 배열:")
print(center_array)
