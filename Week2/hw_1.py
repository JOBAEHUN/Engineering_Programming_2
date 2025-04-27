money = int(input("금액을 입력하시오: ")) # 지폐로 바꿀 금액 입력

money_50k = money // 50000 # //는 정수의 몫을 구하는 연산자
money %= 50000
money_10k = money // 10000
money %= 10000
money_5k = money // 5000
money %= 5000
money_1k = money // 1000
money %= 1000

if money_50k:
    print(f"50000원 {money_50k}장", end=", ")
if money_10k:
    print(f"10000원 {money_10k}장", end=", ")
if money_5k:
    print(f"5000원 {money_5k}장", end=", ")
if money_1k:
    print(f"1000원 {money_1k}장")

print("\n")

if money:
    print(f"지폐로 바꾸지 못한 금액은 {money}원입니다.")
else:
    print("모든 금액을 지폐로 바꿨습니다.")

