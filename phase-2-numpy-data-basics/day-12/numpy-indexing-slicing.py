import numpy as np

arr = np.array([10,20,30,40,50])

print(arr)
print(arr[0])
print(arr[2])
print(arr[-1])
print(arr[0:3])
print(arr[0:5:2])

arr[1] = 300
print(arr)


matrix = np.array([[1,2,3],
[4,5,6],
[7,8,9]
])

print(matrix)
print('access row:\n',matrix[1])
print('accsess ele in row:\n',matrix[2][2])
print('Column Access:\n',matrix[:,1]) # : → all rows #1 → second column
print('Sub-Matrix:\n', matrix[1:2,1:2])
print('Sub-Matrix:\n', matrix[1:3,2:3])
print('Sub-Matrix:\n', matrix[1:3,1:3])




