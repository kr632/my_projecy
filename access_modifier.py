# public access modifier
# private access modifier
# protected access modifier


class employee:
    def __init__(self):
        self.name = "kunal"

a = employee()
print(a.name)
        
  # public attribute

#   In Python, name mangling is a mechanism used to make class attributes harder to access directly from outside the class.

class Student:
    def __init__(self):
        self.__name = "Kunal"

s = Student()

print(s._Student__name)   # ❌ Error




       

   