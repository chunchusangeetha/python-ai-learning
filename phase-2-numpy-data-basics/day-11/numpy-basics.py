import numpy as np

arr = np.array([1,2,3,5,2])

print(arr)
print("Shape:", arr.shape)
print("Dimension:", arr.ndim)
print("Data type:", arr.dtype)
print("Size:", arr.size)

arr2 = np.array([[1,7,8],[5,68,9]])

print(arr2)
print("Shape:", arr2.shape)
print("Dimension:", arr2.ndim)
print("Data type:", arr2.dtype)
print("Size:", arr2.size)

arr0 = np.zeros((2,3))
print(arr0)

arr1 = np.ones((2,3))
print(arr1)

arr = np.arange(1,10)
print(arr)

arr = np.linspace(0,10,4)
print(arr)

arr = np.random.rand(3,3)
print(arr)


arr = np.array([1,2,3])
print(arr.dtype)

arr = arr.astype(float)
print(arr)
print(arr + 5) #vectorization - apply to all ele
print(arr * 2)

arr = np.array([10,20,30,40])
print("Sum:", arr.sum())
print("Mean:", arr.mean())
print("Max:", arr.max())
print("Min:", arr.min())