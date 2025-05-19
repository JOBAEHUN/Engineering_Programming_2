import matplotlib.pyplot as plt
import numpy as np

plt.plot(np.random.randn(10),'k',label='one')
plt.plot(np.random.randn(10)*3, 'r--',label='two')
plt.plot(np.random.randn(10)*3, 'r--',label='three')

plt.legend()
plt.show()
