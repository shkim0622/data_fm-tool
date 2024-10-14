import json
with open('json1.json') as f:
    data = json.load(f)
    
print(type(data))
print(data)
new_data = {'person3': [{'name': 'C','age': 30,'cmd': 'happy','value': 300}]}
data.update(new_data)

with open('json2.json','w') as f:
    json.dump(data, f, indent=2)