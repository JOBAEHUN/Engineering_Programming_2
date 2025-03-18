"""
Created on Mon Mar 17 09:33:58 2025

@author: BaeHun
"""

list1 = []
list2 = []
value = 1
for i in range(0,3):
    for k in range(0,4):
        list1.append(value)
        value +=1
    list2.append(list1)
    list1 = []
    
for i in range(0,3):
    for k in range(0,4):
        print("%3d" % list2[i][k], end = " ")
    print("")
    
print("\n")
    
list1 = []
list2 = []
value = 0
for i in range(0,4):
    for k in range(0,5):
        list1.append(value)
        value = value + 3
    list2.append(list1)
    list1 = []

for i in range(0,4):
    for k in range(0,5):
        print("%3d" % list2[i][k], end = " ")
    print("")    
    
    
    
    
    
    
    
    