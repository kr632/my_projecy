from os import read
from turtle import update


class myclass:
    def __init__(self, name):
        self.__name = name

    def show(self):
        print(f"Name: {self.__name}")
    @property
    def ten_value(self):        #getter  
        return 10*self.__name 
    
    @ten_value.setter         
    def ten_value(self, value):        self.__name = value/10
    


obj = myclass(15)
obj.ten_value = 150
print(obj.ten_value)
obj.show()

# Getter = read
# Setter = write/update


