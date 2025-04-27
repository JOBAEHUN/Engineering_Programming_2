def sum_list(a):
    j = 0
    for i in a:
        j = j + i
    print(j)

list_a = [1,2,3,4,5,6,7,8,9,10]
sum_list(list_a)

def sum_list_r(a):
    j = 0
    for i in a:
        j = j + i
    return j
result = sum_list_r(list_a)
print("합계는", result)

