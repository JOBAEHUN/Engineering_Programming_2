"""
Created on Sun Apr 27 00:27:42 2025

@author: BaeHun
"""

u = [2,2]
v = [2,3]
z = [3,5]
result = []

for i in range(len(u)):
    result.append(u[i] + v[i] + z[i])

print(result)

result = [sum(t) for t in zip(u,v,z)]
print(result)

def vector_addition(*args):
    return [sum(t) for t in zip(*args)]

print(vector_addition(u,v,z))

