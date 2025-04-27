"""
Created on Sun Apr 27 00:20:08 2025

@author: BaeHun
"""

def asterisk_test(a, *args):
    print(a, args)
    print(type(args))

def asterisk_test1(a, **kargs):
    print(a, kargs)
    print(type(kargs))
    
def asterisk_test2(a, args):
    print(a, *args)
    print(type(args))
    
asterisk_test(1,2,3,4,5,6)
asterisk_test1(1, b=2, c=3, d=4, e=5, f=6)
asterisk_test2(1, (2,3,4,5,6))

a,b,c = ([1,2], [3,4], [5,6])
print(a,b,c)

data = ([1,2], [3,4], [5,6])
print(*data)

for data in zip(*[[1,2],[3,4], [5,6]]):
    print(data)
    print(type(data))

def asterisk_test3(a,b,c,d):
    print(a,b,c,d)
data = {"b": 1, "c":2, "d": 3}
asterisk_test3(10, **data)