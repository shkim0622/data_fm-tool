import pandas as pd

data = pd.Series([1,2,3,4,5])
print(data)

data2 = pd.Series({1:1,2:2,3:3,4:4,5:5})
print(data2)

data3=pd.Series(['A',10,'hello',40])
print(data3)

data4=pd.Series(['A',10,'hello',40],index = ['name','age','cmd','value'])
print(data4)

print('name : ',data4.at['name'])