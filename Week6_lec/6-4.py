"""
Created on Sun Apr 27 00:09:16 2025

@author: BaeHun
"""

iteration_max =10000

vector = list(range(iteration_max))
scalar = 2

for _ in range(iteration_max):
    result = [scalar * value for value in vector]
    