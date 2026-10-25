class person:
    def __init__(self, name, age, networth):
        self.name = name
        self.age = age
        self.networth = networth


a = person("john", 36, 10)
b = person("michael", 30, 20)
print(a.name)
print(a.age)
print(a.networth)
print(b.name)
print(b.age)
print(b.networth)

we use self to automatically refer to the instance of the class, 
    
    # __init__() is a special method that runs automatically when you create an object from a class.

# classes make things cleaner and scalable