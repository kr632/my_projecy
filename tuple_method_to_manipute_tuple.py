# append is use to add an elemnt in the tupple

# a = ("kunal", "rohan", "mohit")
# a = list(a)
# a.append("sahil")
# a = tuple(a)
# print(a)

# # .pop is use to remove an element from the tupple

# a = ("kunal", "rohan", "mohit")
# a = list(a)
# a.append("sahil")
# a.pop(1)
# a = tuple(a)
# print(a)
      
    #   we can also create new tupple and mix the tuple to create new tupple

    #   count method is use the count the number of times an element is present in the tupple
    #   .count() is the code for that

a = ("kunal", "rohan", "mohit", "kunal")
print(a.count("kunal"))

# index method is use to find the index of the element in the tupple
# .index() is the code for that

a = ("kunal", "rohan", "mohit", "kunal")
print(a.index("rohan"))

# for find a index in given range we use .index() and we have to give the range in the argument

a = (1,3,2,2,5,6,6,4)
k = a.index( 2, 0, 5)
print(k)


