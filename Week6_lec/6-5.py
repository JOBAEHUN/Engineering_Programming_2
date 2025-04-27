"""
Created on Sun Apr 27 00:10:50 2025

@author: BaeHun
"""

alist = ['a1','a2','a3']
blist = ['b1','b2','b3']
for i, (a,b) in enumerate(zip(alist,blist)):
    print(i,a,b)