matrix_a = [[1,1],[1,1]]
matrix_b = [[1,1],[1,1]]
print(all([row[0] == value for t in zip(matrix_a, matrix_b) for row in zip(*t) for value in row]))

matrix_b = [[5,8],[6,7]]
print(all([all([row[0] == value for value in row]) for t in zip(matrix_a,matrix_b) for row in zip(*t)]))
