import pickle
data={}
data['person1'] = [{'name': 'A', 'age': 10, 'cmd': 'hello', 'value': 100}] 
data['person2'] = [{'name': 'B', 'age': 20, 'cmd': 'world', 'value': 200}]
data['person3'] = [{'name': 'C', 'age': 30, 'cmd': 'happy', 'value': 300}]

with open ('pickle1.pkl','wb') as fd:
    pickle.dump(data ,fd)
 
with open ('pickle1.pkl','rb') as fr:
    data_read = pickle.load(fr)

print(data_read)