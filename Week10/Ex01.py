import numpy as np
import matplotlib.pyplot as plt

#CSV 파일 불러오기
data = np.loadtxt('data2000.csv', delimiter=',', skiprows=1)

x = data[:,0]
y = data[:,1]

A = np.vstack([x, np.ones(len(x))]).T
a, b= np.linalg.lstsq(A, y, rcond=None)[0]

print(f"기울기(a): {a}")
print(f"절편(b): {b}")

# 시각화
plt.scatter(x, y, color='blue', label='Data')
plt.plot(x, a*x + b, color='red', label='Fitted Line')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Least Squares Fit')
plt.grid()
plt.show()
