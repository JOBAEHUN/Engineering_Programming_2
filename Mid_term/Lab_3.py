def check_prime_num(x):
    for i in range(2,x):
        if x % i == 0:
            # x가 i로 나누어 떨어지면 실행하기
            return False
    return True

number = int(input('판별할 자연수를 입력하세요.'))
print(check_prime_num(number))
