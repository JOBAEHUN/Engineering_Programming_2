import numpy as np

a = np.array([3, 2, 5, 1, 4])
print('원본\n',a)
print('정렬후\n',np.sort(a))
print('원본\n',a)
print('정렬한인덱스\n',np.argsort(a))
a.sort( )
print('원본\n',a)