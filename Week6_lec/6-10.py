"""
Created on Sun Apr 27 00:31:21 2025

@author: BaeHun
"""

u = [1,2,3]
v = [4,4,4]
alpha = 2

result = [alpha * sum(t) for t in zip(u,v)]
print(result)

# 시험 문제 낼꺼임
matrix_a = [[3,6], [4,5]]
matrix_b = [[5,8], [6,7]]
result = [[sum(row) for row in zip(*t)] for t in zip(matrix_a,matrix_b)]
print(result)
