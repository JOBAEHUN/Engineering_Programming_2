"""
Created on Mon Mar 17 10:18:38 2025

@author: BaeHun
"""

def calc(v1,v2,op):
    result = 0
    if op == '+':
        result = v1 + v2
    elif op == '-':
        result = v1 - v2
    elif op == '*':
        result = v1 * v2
    elif op == '/':
        result = v1 / v2
    
    return result
print(calc(10,20,'/'))

## 변수 선언 부분 ##
res = 0
var1, var2, oper = 0,0, ""

## 메인 코드 부분 ##
oper = input("게산을 입력하세요(+,-,*,/) : ")
var1 = int(input("첫 번째 수를 입력하세요 : "))
var2 = int(input("두 번째 수 를 입력하세요 : "))

res = calc(var1,var2,oper)

print("## 계산기 : %d %s %d = %d" % (var1,oper,var2,res))
