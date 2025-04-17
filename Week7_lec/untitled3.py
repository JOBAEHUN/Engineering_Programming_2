"""
Created on Mon Apr 14 09:32:02 2025

@author: BaeHun
"""

import numpy as np
ary = np.arange(10)
ary[0] = 100
print(ary)
ary_sub1 = ary[3:7]
print(ary_sub1)
ary_sub1[:] = 77
print(ary_sub1)
print(ary)