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

with open ('pickle1.pkl','wb') as fd:
    pickle.dump(person1 ,fd)
    pickle.dump(person2 ,fd)
    pickle.dump(person3 ,fd)
 