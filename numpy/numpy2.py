import numpy as np

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

np.savez('./numpy2',arr1=arr1,arr2=arr2)

arr_load = np.load('numpy2.npz')
print('arr1 :',arr_load['arr1'])
print('arr2 :',arr_load['arr2'])

