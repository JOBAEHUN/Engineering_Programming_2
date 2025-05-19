import matplotlib.pyplot as plt
import numpy as np

plt.subplot(2, 2, 1) # 2행2열중첫번째그래프
plt.plot(np.random.randn(10), 'b--')
plt.subplot(2, 2, 2) # 2행2열중두번째그래프
plt.plot(np.random.randn(100), 'r', alpha=0.7)
plt.subplot(2, 2, 3) # 2행2열중세번째그래프
plt.plot(np.random.randn(10), 'y^')
plt.subplot(2, 2, 4) # 2행2열중네번째그래프
plt.plot(np.random.randn(10), 'g.')
plt.show()
