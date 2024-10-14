import csv

with open ('csv3.csv','r') as f:
    read = csv.DictReader(f)
    
    data=list(read)
    print(data)
        
    f.close()