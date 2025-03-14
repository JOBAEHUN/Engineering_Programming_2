money = int(input("금액을 입력하시오.")) # 지폐로 바꿀 금액 입력

money_50k = money // 50000 # //는 정수의 몫을 구하는 연산자
money = money - money_50k*50000 # moeny 변수를 다시 저장
money_10k = money // 10000
money = money - money_10k*10000
money_5k = money // 5000
money = money - money_5k*5000
money_1k = money // 1000
money = money - money_1k*1000
print("50000원 {0}장,10000원 {1}장,5000원 {2}장, 1000원 {3}장".format(money_50k,money_10k,money_5k,money_1k))
print("지폐로 바꾸지 못한 금액은 {}원입니다.".format(money))
