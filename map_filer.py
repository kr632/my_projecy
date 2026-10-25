# The map() function in Python is used to apply a function to every item in an

# iterable (like a list, tuple, etc.) and return a new iterable with the results.

# we can also use lambda function to do the same thing

from functools import reduce


def cube(x):
    return x ** 3

print(cube(2))

i = []
kun = list(map(cube,i))
print(kun)

# The filter() function in Python is used to\
#  select only those elements from an
# iterable (like a list) that satisfy a condition.

def is_even(x):
    return x % 2 == 0

numbers = [1,6,4,4,5,6,7,8,9,10]

result = filter(is_even, numbers)

print(list(result))

# predicate function is simply a function that returns either True or False.

# The reduce() function in Python is used to apply a function 
# cumulatively to the items of an iterable, reducing it to a single value.

# reduce() → combine all items into one

# but first we need to import reduce from functools module

from functools import reduce

numbers = [1, 2, 3, 4]

result = reduce(lambda x, y: x + y, numbers)

print(result)