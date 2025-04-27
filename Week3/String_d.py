ss = 'Python is Easy. 그래서 programming이 재미있습니다. ^^'
print(ss.upper())
print(ss.lower())
print(ss.swapcase())
print(ss.title())

ss = '----파---이---썬----'
print(ss.strip('-'))
ss = '<<<파 << 이 >> 썬>>>'
print(ss.strip('<>'))

ss = '열심히 파이썬 공부 중~~'
ss.replace('파이썬' , 'Python')
print(ss)

ss = 'Python을 열심히 공부 중'
print(ss.split())
ss = '하나:둘:셋'
print(ss.split(':'))
ss = '하나\n둘\n셋'
print(ss.splitlines())
ss ='%'
print(ss.join('파이썬'))

before = ['2019', '12', '31']
after = list(map(int, before))
print(after)

