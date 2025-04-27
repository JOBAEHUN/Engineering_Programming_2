"""
Created on Mon Mar 17 09:52:22 2025

@author: BaeHun
"""

'''
ss = '파이썬짱!'

sslen = len(ss)
for i in range(0,sslen):
    print(ss[i]+ '$',end ='')
'''

### Self Study 3-4

sss = '파이썬은재밌어요'
sslen = len(sss)
for i in range(0,sslen):
    if i // 2 == 1:
        print(sss[i]+ '#',end ='')

'''        
위코드를수정하여‘파이썬은재미있어요’에서‘파#썬#재#있#요’를출력해보자.즉
짝수번째글자는그대로출력되고,홀수번째글자는#이표시되도록한다.
 Hint: If문을사용하여처리한다. 짝수는2로나누어서나머지값이0이면짝수이다.
'''