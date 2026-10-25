from math import *
import math
result = sqrt(16) * pi
print(result)


# * is used to import all the functions from a module.
# as is used to give a different name to the module while importing it. For example, 
from math import sqrt as kunal
result = kunal(16) * pi
print(result)

# dir function is used to see all the functions in a module. For example,
print(dir(math))