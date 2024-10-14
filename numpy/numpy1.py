import numpy as np

x =  np.array([[1,2],[4,5]])
np.save('./numpy1',x)

x_s=np.load('./numpy1.npy')
print(x_s)