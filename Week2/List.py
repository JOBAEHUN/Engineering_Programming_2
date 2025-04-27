#리스트 생성하기
list_1 = [1,2,3,5,1,3]
list_2 = []
print(list_1)
print(list_2)
print(len(list_1))

#리스트 변경하기
list_1[3] = 9999 # index 3을 9999로 변경
print(list_1)
list_1.append(100) # 리스트 맨 끝에 추가
print(list_1)
list_1.remove(9999) # 9999를 삭제 맨 앞에 있는 요소만 삭제함
print(list_1)
list_1.insert(0,700) # index 0 위치에 700을 삽입
print(list_1) 

list_2 = list_1.copy() # 리스트 복제하기
print(list_2)

list_3 = [897, 2, 1, 4, 99, 5.24, 17]
print(list_3)

list_3.reverse() # 뒤집기
print(list_3)

list_3.sort() # 오름차순 정렬하기
print(list_3)

list_3.sort(reverse=True) # 내림차순 정렬하기
print(list_3)