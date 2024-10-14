import json
data = {'nema':'a','age':1}
with open('json2.json','w') as f:
    json.dump(data,f, indent=2)
