"""
Created on Mon Mar 17 10:18:38 2025

@author: BaeHun
"""

def calc(v1,v2,op):
    result = 0
    if op == '+':
        result = v1 + v2
    elif op == '-':
        result = v1 - v2
    elif op == '*':
        result = v1 * v2
    elif op == '/':
        result = v1 / v2
    
    return result
print(calc(10,20,'/'))
