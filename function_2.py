
def calculateGmean(a, b):
    mean = (a + b) / (a * b)
    print(mean)

a = int(input())
b = int(input())
if a > b:
    print("a is greater than b")
else:
    print("b is greater than a")

    calculateGmean(a, b)