# if we have to add something in dictonary so we use .update


info1 = {'kunal':92 , 'abhishek':89}
info2= {'gaurav':25}
info1.update(info2)
print(info1)

# for deleting all the value in dictonary

# info1.clear()
# print(info1)

# pop is use to clear the given value in dictonary

info1.pop('kunal')
print(info1)

# pop item is used to clear last value in dictonary

info1.popitem()
print(info1)


