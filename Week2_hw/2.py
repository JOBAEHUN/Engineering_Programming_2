start, end, step = map(int,input("세 개의 숫자를 입력하세요: ").split()) # 띄어쓰기를 기준으로 입력받기, map함수로 리스트에 넣기
total = 0 # total 변수 0으로 초기화
numbers =[]

for i in range(start,end +1, step): # end+1까지 range를 설정해 end까지 연산이 가능하도록 하기
    total += i
    numbers.append(str(i)) # i 값을 문자열로 변환하여 리스트에 추가
result = " + ".join(numbers)  # 리스트를 문자열로 변환하여 출력 포맷 생성
print(f"{result} = {total}입니다")