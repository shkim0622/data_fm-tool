import numpy as np

arr = np.array([[1,2,3],[4,5,6]])

np.savetxt('./numpy3.txt', arr, fmt='%d', delimiter=' ')
arr_load = np.loadtxt('./numpy3.txt',dtype=int)
print('arr :',arr_load)
print('arr :',arr_load[0])
print('arr :',arr_load[1])




