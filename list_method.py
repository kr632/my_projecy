# list method
# append method of list
# append methos is used to add an element at the end of the list. It takes only one argument which is the element to be added.


lst = [1,2,3,4,5]
lst.append(6)
print(lst)

# sort method of list
# sort method is used to start list from the small number to the big number

lst = [66,55,45,1,2,3,4,5]
lst.sort()
print(lst)

# reverse = True is used to sort the list in reverse order from big number to small number

lst = [66,55,45,1,2,3,4,5]
lst.sort(reverse=True)
print(lst)

# reverse method of list is used to reverse the order of the list

lst = [66,55,45,1,2,3,4,5]
lst.reverse()
print(lst)

# index method is used to find the index of the element in the list. It takes one argument which is the element whose index is to be found.

lst = [66,55,45,1,2,3,4,5]
print(lst.index(45))

#count method is used to count the number of times an element is present in the list. It takes one argument which is the element whose count is to be found.

lst = [66,55,45,1,2,3,4,5,45,45]
print(lst.count(45))

# copy method is used to create a copy of the list. It does not take any argument.

lst = [66,55,45,1,2,3,4,5,45,45]
print(lst.count(45))
m = lst.copy()
print(m)

# append method is used to change the index on given number

lst = [66,55,45,1,2,3,4,5,45,45]
print(lst.count(45))
lst.insert(2,66)
print(lst)


# extend method is used to extent the old list to the new list by adding extra element in the new list

lst = [66,55,45,1,2,3,4,5,45,45]
print(lst)

m = [55,55,5,6]
lst.extend(m)
print(lst)

# concatenate two lists
lst = [66,55,45,1,2,3,4,5,45,45]
m = [55,55,5,6]
lst = lst + m
print(lst)

