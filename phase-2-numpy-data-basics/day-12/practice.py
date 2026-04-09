import numpy as np

arr = np.array([23,56,43,21,67,89])

print('first ele:\n',arr[0])
print('last ele:\n',arr[-1])
print('slice 1:4 :\n',arr[1:4])


matrix = np.array([[20,30,40],
[50,60,70],
[80,90,100]])

print('matrix', matrix)
print('first row:\n',matrix[0])
print('first col:\n',matrix[:,0])
print('middle ele:\n', matrix[1:2,1:2])
print('middle ele:\n', matrix[1,1])
print(matrix.sum())

arr[2] = 500
print('modified arr:\n',arr)
print(arr.sum())