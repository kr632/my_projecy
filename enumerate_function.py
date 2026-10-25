marks = [12.,55,5,5,69,74,1,5,63]



# index = 1
# for mark in marks:
#     print(mark)
#     if (index == 5):
#         print("index awssome")
#     index = index + 1

for index,mark in enumerate(marks, start=4):
    print(mark)
    if (index == 5):
        print("index awssome")

# enumerate() takes a list and gives you:
# (position, value) together

# if we have to change the start value in for loop we use start = 1 inside the enumerate function. By default it starts with 0.