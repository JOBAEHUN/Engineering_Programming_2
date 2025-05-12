import numpy as np
import matplotlib.pyplot as plt

# 데이터 불러오기
data = np.loadtxt('data2000.csv', delimiter=',', skiprows=1)
x = data[:, 0]
y = data[:, 1]

# 초기값
a = 0
b = 0
alpha = 0.0001  # 학습률
epochs = 1000   # 반복 횟수

n = len(x)

# SDM 수행
for _ in range(epochs):
    y_pred = a * x + b
    error = y - y_pred
    loss = np.mean(error ** 2)

    da = -2 * np.sum(x * error) / n
    db = -2 * np.sum(error) / n

    a -= alpha * da
    b -= alpha * db

# 결과 출력
print(f"최종 방정식: y = {a:.4f} * x + {b:.4f}")
print(f"최종 손실: {loss:.3f}")

# 시각화
plt.figure(figsize=(10, 6))
plt.scatter(x, y, label="Data", color="blue")
plt.plot(x, a * x + b, color="red", label=f"y = {a:.2f}x + {b:.2f}")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Steepest Descent Linear Fit")
plt.legend()
plt.grid(True)
plt.show()