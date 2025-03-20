"""
Created on Thu Mar 20 15:05:17 2025

@author: BaeHun
"""

import math #math 모듈 호출

print(("""연산을 선택하세요:
1: 덧셈 (x + y), 2: 뺄셈 (x - y), 3: 곱셈 (x * y), 
4: 나눗셈 (x / y)
5: 로그 (log_x(y), 여기서 x는 밑(base), y는 대상 값(value), e 입력 가능)
6: 지수 (x^y, x에 e 입력 시 e^y)  
"""))
oper = int(input("번호 입력: "))
num_a = input("첫번째 수 (x)를 입력하세요: ")
num_b = input("두번째 수 (y)를 입력하세요: ")

if num_a == "e":
    num_a = math.e
    num_a = round(float(num_a),3)
else:
    num_a = float(num_a)
    
if num_b == "e":
    num_b = math.e
    num_b = round(float(num_b),3)
else:
    num_b = float(num_b)
    
'''
if num_a == "e":
    num_a = math.e
    num_a = round(float(num_a),3)
elif num_b == "e":
    num_b = math.e
    num_b = round(float(num_b),3)   
else:
    num_a = float(num_a)
    num_b = float(num_b)
'''


if oper == 1: 
        result = num_a + num_b
        print(f"## 계산기: {num_a} + {num_b} = {result}")
    
elif oper == 2:
        result = num_a - num_b
        print(f"## 계산기: {num_a} - {num_b} = {result}")
elif oper == 3:
        
        result = num_a * num_b
        print(f"## 계산기: {num_a} * {num_b} = {result}")
elif oper == 4:
    if num_b == 0:
        print("오류: Division by zero")
    else: 
        result = round((num_a / num_b),3)
        print(f"## 계산기: {num_a} / {num_b} = {result}")
elif oper == 5:
    result = math.log(num_a, num_b) 
    print(f"## 계산기: log_{num_a}({num_b}) = {result}")
elif oper == 6:    
    result = num_a ** num_b
    print(f"## 계산기: {num_a} ^ {num_b} = {result}")
    
'''
오류가 났을 때 다음 구문을 활용할 것
print(num_a,num_b)
print(type(num_a),type(num_b))
'''