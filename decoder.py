# decorator is use to modify function

from local_vs_global_variables import name


def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

# *args and **kwargs are used to pass a variable number of arguments to a function.

# The * symbol: Think of the asterisk as a vacuum cleaner. It sucks up every single
# number you throw at the function and packs them into a single container

# Fixed arguments
def add_two(a, b):
    return a + b

# Variable arguments with *args
def add_everything(*args):
    return sum(args)

print(add_everything(1, 2))        # Result: 3
print(add_everything(10, 5, 5, 20)) # Result: 40

def build_profile(name, **kwargs):
    print(f"Character: {name}")
    print(f"Extra Stats: {kwargs}")

# Now you can pass as many labeled pieces of info as you want
build_profile("Archer", level=10, health=100, weapon="Bow")


def my_function(*args, **kwargs):
    print(args)
    print(kwargs)

my_function(1, 2, 3, apple=5, orange=10)


# args are plain values and kwargs are labeled values.

# A Shopping Bag: You just throw items in.
# A Contact List: Every number has a name attached.

