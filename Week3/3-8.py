'''
ss = '파이썬짱!'

sslen = len(ss)
for i in range(0,sslen):
    print(ss[i]+ '$',end ='')
'''

### Self Study 3-4
### ‘파이썬은재미있어요’에서‘파#썬#재#있#요’를출력해보자.

sss = '파이썬은재미있어요'
sslen = len(sss)
for i in range(0,sslen):
    if i % 2 == 0:
        print(sss[i],end ='')
    else:
        print('#',end = '')


