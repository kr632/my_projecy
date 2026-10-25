class employee:
    name = "john"
    def __len__(self):
        i = 0
        for char in self.name:
            i += 1
        return i
    

e = employee()
print(e.name)
print(len(e))
        
