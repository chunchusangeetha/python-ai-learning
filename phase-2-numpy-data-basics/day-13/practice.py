import numpy as np

arr = np.array([10,20,47,42,27])

print('original arr:\n',arr)
print('add 5 to arr:\n',arr+5)
print('arr mul by 5 :\n',arr*5)

arr1 = np.array([56,43,87,65,85])
arr2 = np.array([43,43,67,34,68])

print('sum of arra1 and arr2:\n', arr1+arr2)
print('mul of arra1 and arr2:\n', arr1*arr2)

matrix = np.array([[2,5,7],
[4,7,3],
[6,9,1]])

result = np.dot(matrix,matrix)
print('matrix Multiply with itself:\n',result)