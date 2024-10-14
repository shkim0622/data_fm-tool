import csv

data = [['id','name','value','age'],
        [1,'A',100,10]]

with open('csv2.csv','w') as f:
    writer=csv.writer(f)
    writer.writerows(data)
    f.close()