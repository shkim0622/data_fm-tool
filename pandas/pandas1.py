import pandas as pd

value =[['A','B'],[10,20],['hello','world'],[100,200]]
index =  ['name','age','cmd','value']
columns = ['person1','person2']

data=pd.DataFrame(value,index=index, columns=columns)
print(data)

