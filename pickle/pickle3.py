import pickle
class Person:
    def __init__(self,name, age, cmd, value):
        self.name = name
        self.age = age
        self.cmd =cmd
        self.value =  value
    
    def print (self):
        print(self.name,self.age,self.cmd,self.value)

person1 = Person('A',10,'hello', 100) 
person2 = Person('B',20,'world', 200) 
person3 = Person('C',30,'happy', 300) 
 
with open ('pickle1.pkl','rb') as fr:
    person1 = pickle.load(fr)
    person2 = pickle.load(fr)
    person3 = pickle.load(fr)

print(person1.name)
print(person2.value)
print(person3.age)
