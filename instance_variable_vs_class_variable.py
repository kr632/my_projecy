
class age:
    cpmpany_name = "ABC Corp"  # class variable
    student_no = 0
    
  # class variable
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.increment_amount = 0.2
    def show(self):
        print(f" Name: {self.name}, Age: {self.age}, Increment Amount: {self.increment_amount}, Company: {age.cpmpany_name}, Student No: {age.student_no}")


        age.student_no += 1


a1 = age("John", 25)
a1.increment_amount = 0.5
a1.show()
a2 = age("Alice", 30)
a2.show()

# instance variable = object ke andar hota hai, har object ka apna alag hota hai
# class variable = class ke andar hota hai, sabhi objects ke liye same hota