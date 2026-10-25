# recurtion is used when a function calls itself. It is a powerful tool for solving problems that can be broken down into smaller, similar subproblems. A recursive function typically has two main components: a base case that stops the recursion, and a recursive case that breaks the problem into smaller parts and calls itself.
    
# # foctorial means (7) = 7*6*5*4*3*2*1 = 5040

def factorial(n):
    if n == 0 or n == 1:  
        return 1
    else:
        return n * factorial(n - 1) 
    
print(factorial(5))

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 2 or n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(8))

# fabonacci is sequence postion of index number which we given