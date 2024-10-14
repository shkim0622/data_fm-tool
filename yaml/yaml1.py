import yaml
with open('coco128.yaml','r') as f:
    a = yaml.load(f,Loader=yaml.FullLoader) 
    print("org : ", a)
    
data = {'person2': [{'name': 'C','age': 30,'cmd': 'happy','value': 300}]}
a.update(data)

with open('yaml1_new.yaml','w') as f:
    yaml.dump(a,f)
    print("dump: ",a)