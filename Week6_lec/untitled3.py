"""
Created on Mon Apr  7 09:57:28 2025

@author: BaeHun
"""

matrix_a= [[1, 1, 2], [2, 1, 1]]
matrix_b= [[1, 1], [2, 1], [1, 3]]
result = [[sum(a * b for a, b in zip(row_a, column_b)) for column_b in zip(*matrix_b)] for row_a in matrix_a]
print(result)
