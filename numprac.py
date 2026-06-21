import numpy as np
print (np.__version__)
arr = np.array([[1, 2, 3], [4, 5, 6]])  
print(arr)
print(type(arr))
print(arr.ndim)
new_arr = arr.astype(float)
print(new_arr)

arr1 = np.array([[1, 2], [3, 4]])
arr2 = arr1.copy()
arr2[0][0] = 100
print(arr1)
print(arr2)

for x in np.nditer(arr):
  print(x)