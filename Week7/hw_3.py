import numpy as np
import os

# 0부터 255 사이의 정수로 이루어진 5000x5000 배열 생성
array = np.random.randint(0, 256, size=(5000, 5000), dtype=np.uint8) 


np.save("array.npy", array) # .npy 형식으로 저장
np.savez("array.npz", arr=array)
np.savez_compressed("array_compressed.npz", arr=array)

size_npy = os.path.getsize("array.npy")
size_npz = os.path.getsize("array.npz")
size_compressed = os.path.getsize("array_compressed.npz")

print("파일 크기 비교 (바이트 단위):")
print(f"array.npy: {size_npy} bytes")
print(f"array.npz: {size_npz} bytes")
print(f"array_compressed.npz: {size_compressed} bytes")
