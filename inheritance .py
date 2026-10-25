class employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def showasd(self):
        print(f"Name: {self.name}, Salary: {self.salary}")


class manager(employee):
    def showkunal(self):
        print(f"Manager Name: {self.name}, Salary: {self.salary}")
        

e1 = employee("John", 50000)
e1.showasd()
e2 = manager("Alice", 80000)
e2.showkunal(

    # Ek class dusri class ke properties aur methods inherit (reuse) kar sakti hai.

    # Inheritance = "I already have this code, let me extend it instead of rewriting it."

        