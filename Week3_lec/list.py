"""
Created on Mon Mar 17 09:26:45 2025

@author: BaeHun
"""

my_list = [30,10,20]
print(f"현재 리스트는 {my_list} 입니다.")

my_list.append(40)
print(f"그 다음 리스트는 {my_list} 입니다.")

print(f"pop()으로 추출한 값 {my_list.pop()}")
print(f"pop()으로 추출한 다음 리스트는 {my_list} 입니다.")

my_list.sort()
print(f"리스트는 {my_list} 입니다.")

my_list.reverse()
print(f"리스트는 {my_list} 입니다.")
