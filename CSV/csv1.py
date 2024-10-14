import csv

with open('csv1.csv','r') as f:
    data = csv.reader(f)
    for i in data:
        print(i)
    f.close()

with open('csv1.csv','a') as f:
    data = csv.writer(f)
    data_new = ['C',10,'happy',300]
    data.writerow(data_new)
    print(data_new)
    f.close()
    