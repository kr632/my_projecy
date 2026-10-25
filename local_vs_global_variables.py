x = 5 
print(x)

def name():
    global x
    x = 10 
    print(f"the local variable is {x}")

name()
print(f"the global variable is {x}")

# local variables are defined inside a function and
#  can only be accessed within that function.
#  Global variables are defined outside of any function and 
# can be accessed throughout the entire program.

# we can use the global keyword to modify a global variable inside a function.