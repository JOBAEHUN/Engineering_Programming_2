# 구구단을 하기 위한 알고리즘 for loop 2번 쓰기
for i in range(1,10):
    print("##{}단##".format(i))
    for j in range(1,10):
        print("{0} x {1} = {2}".format(i,j,i*j))
