iteration_max =10000

vector = list(range(iteration_max))
scalar = 2

for _ in range(iteration_max):
    result = [scalar * value for value in vector]
    