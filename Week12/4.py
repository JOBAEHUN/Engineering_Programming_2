import matplotlib.pyplot as plt

year = [2014,2017,2020,2023]
price = [25000, 31000, 53000, 63000]
plt.plot(year,price, 'rs:')

plt.axis([2013,2024,20000,70000])
plt.show()