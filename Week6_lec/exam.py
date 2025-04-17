"""
Created on Mon Apr  7 09:47:23 2025

@author: BaeHun
"""

# 시험 문제 낼꺼임
matrix_a = [[3,6], [4,5]]
matrix_b = [[5,8], [6,7]]
result = [[sum(row) for row in zip(*t)] for t in zip(matrix_a,matrix_b)]
print(result)
