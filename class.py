# class is blueprint for creating objects
class person:
    name = "john"
    age = 36
    networth = 10

a = person()
print(a.name)
print(a.age)
print(a.networth) 

# self is used to refer to the current instance of the class,
#  and is used to access variables that belongs to the class. 
#  It does not have to be named self , you can call it whatever you
#  like, but it has to be the first parameter of any function in the class:

class person:
    def __init__(self, name, age, networth):
        self.name = name
        self.age = age
        self.networth = networth


