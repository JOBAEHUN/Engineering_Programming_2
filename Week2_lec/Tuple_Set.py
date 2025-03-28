"""
Created on Tue Mar 25 10:42:28 2025

@author: BaeHun
"""

""" 튜플은 괄호 없이 쉼표로 나타낼 수 있다.
tupel_1 = 1, 2, 3, 4, 5
tupel_2 = '파이썬', 10000, False
"""

""" 튜플은 리스트와 다르게 한번 할당하면 값을 변경하거나 삭제할 수 없다.
tuple_1 = 1, 2, 3, 4, 5
tuple_1[2] = 100 # 실행 안될 것임
"""

tuple_1 = 1, 2, 3, 4, 5
print(len(tuple_1)) #length 함수

set_1 = {1, 2, 3, '가', '나', '다'}
set_2 = set({1, 2, 3, '가', '나', '다', 1, 2})
set_3 = set([1, 2, 3, '가', '나', '다', 3])

#set는 데이터 중복을 허용하지 않는다.

print(set_1)
print(set_2)
print(set_3)

print('\n')

set_1.add('추가')
print(set_1)
set_1.remove('가')
print(set_1)
set_copy_1 = set_1.copy()
print(set_copy_1)
set_copy_1.clear()
print(set_copy_1)
