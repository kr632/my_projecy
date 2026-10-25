marks = [1,3,2,4,5,6,9,6,8,7]
print(marks[1:6])
print(marks[1:6:3])

# list comprihension
# ind = [i*i for i in range(10)]
# print(ind)

ind = [i*i for i in range(10)if i%3==0]
print(ind)