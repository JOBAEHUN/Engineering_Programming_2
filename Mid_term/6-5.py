alist = ['a1','a2','a3']
blist = ['b1','b2','b3']
for i, (a,b) in enumerate(zip(alist,blist)):
    print(i,a,b)