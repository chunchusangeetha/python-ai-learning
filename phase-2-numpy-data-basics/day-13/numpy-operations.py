import numpy as np

arr = np.array([10,25,38,67,50,7,32])

print('original array:\n', arr)

print('add 5 to arr:\n',arr+5)

print('mul 2 to arr:\n', arr*2)

print("Subtract 10:\n", arr - 10)

a = np.array([1,2,3])
b = np.array([4,5,6])

print("Addition:", a + b)
print("Multiplication:", a * b)

data = np.array([26,62,24,64,8,7,15,5])

print('data:\n',data)
print('sum of data:\n',data.sum())
print('mean of data:\n',data.mean())
print('max of data:\n',data.max())
print('min of data:\n',data.min())
print('Standard Deviation: of data:\n',data.std())

matrix1 = np.array([[1,2,3],
[4,6,8],
[3,5,9]])

matrix2 = np.array([[14,21,32],
[42,64,85],
[32,58,96]])

result = np.dot(matrix1,matrix2)
print('result:\n',result)
print('transpose of matix1:\n',matrix1.T)

matrix = np.array([
    [1,2,3],
    [4,5,6]
])

vector = np.array([10,20,30])
print("Broadcasting result:")
print(matrix + vector)