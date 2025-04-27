import numpy as np

## 넘파이 2차원 배열 생성
SIZE = 3
numpyAry = np.random.randint(0, 255, size=(SIZE, SIZE))

## 배열 출력
print(numpyAry)
print()

## 배열 값 2배 증가
numpyAry = numpyAry * 2

## 배열 출력
print(numpyAry)
print()

## for문으로 평균값 계산
total = 0
count = 0

for i in range(SIZE):
    for k in range(SIZE):
        total += numpyAry[i][k]
        count += 1

average = total / count
print(f"평균 값 --> {average:.1f}")
