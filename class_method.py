class employee:
    company = "google"
    def getSalary(self):
        print(f"salary of {self.name} for {self.company} is 100000")

    @classmethod
    def getCompany(cls, new_company):
        cls.company = new_company


e1 = employee()
e1.name = "john"
e1.getSalary()
e1.getCompany("apple")
e1.getSalary()
print(employee.company)


# the first parameter we use in class is cls, it is used to refer to the class itself.
# the first parameter we use in instance methods is self, it is used to refer to the instance of the class.

# class method as alternative constructor


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, data):
        name, age = data.split(":")
        return cls(name, int(age))

s1 = Student.from_string("Kunal:25")

print(s1.name)
print(s1.age)
