"""
Created on Sat Apr 26 14:58:28 2025

@author: BaeHun
"""

def calc(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b == 0:
            print("0으로는 나누면 안 됩니다.ㅠㅠ")
            return None
        else:
            return a / b
    elif op == '**':
        return a ** b
    else:
        print("지원하지 않는 연산자입니다.")
        return None

# 메인 코드
var1 = int(input("첫 번째 수를 입력하세요 : "))
oper = input("계산을 입력하세요(+,-,*,/,**) : ")
var2 = int(input("두 번째 수를 입력하세요 : "))

res = calc(var1, var2, oper)

if res is not None:
    print("## 계산기 : %d %s %d = %s" % (var1, oper, var2, res))
