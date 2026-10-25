# lembda_function is small anonymous function

# def double(x):
#     return x * 2



def kunal(fx,value):
    return 6 * fx(value)

double = lambda x: x * 2
average = lambda x, y: (x + y) / 2

print(double(57))
print(average(10, 20))
print(kunal(double, 57))

# Think of it like this:

# double is a function waiting for a value
# You call it: double(57)
# Python assigns:

