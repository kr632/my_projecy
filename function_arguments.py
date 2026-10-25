# def calculate(a,b):
#     print("the sun of", (a+b)/2)

# calculate(a=):

def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    print("average is: ", sum/len(numbers))

average(1,2,3)