"""
Created on Mon Mar 17 10:12:18 2025

@author: BaeHun
"""

user_input = input("문자열 입력 : ")

has_alpha = any(char.isalpha() for char in user_input)
has_digit = any(char.isdigit() for char in user_input)
has_special = any(not char.isalnum() for char in user_input)

if has_alpha and has_digit and not has_special:
    print("글자+숫자입니다.")
elif has_alpha and not has_digit and not has_special:
    print("글자입니다.")
elif not has_alpha and has_digit and not has_special:
    print("숫자입니다.")
elif has_special:
    print("모르겠습니다.")
else:
    print("모르겠습니다.")

    