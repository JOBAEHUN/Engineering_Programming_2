"""
Created on Thu Apr 17 13:58:05 2025

@author: BaeHun
"""

import numpy as np
import os

# 1. 배열 생성
array = np.random.randint(0, 256, size=(5000, 5000), dtype=np.uint8)

# 2. 저장
np.save("array.npy", array)
np.savez("array.npz", arr=array)
np.savez_compressed("array_compressed.npz", arr=array)

# 3. 파일 크기 비교
size_npy = os.path.getsize("array.npy")
size_npz = os.path.getsize("array.npz")
size_compressed = os.path.getsize("array_compressed.npz")

# 4. 출력
print("파일 크기 비교 (바이트 단위):")
print(f"array.npy: {size_npy} bytes")
print(f"array.npz: {size_npz} bytes")
print(f"array_compressed.npz: {size_compressed} bytes")
