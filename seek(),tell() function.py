# with open("sample.txt", "r") as f:
#     print(type(f))
#     f.seek(10)
#     print(f.tell())
#     data = f.read()
#     print(data)

    # seek functions allow you move to read the current possition of file
    
    
    #this function to tracking the position of file f.tell() 
    # function return the current position of file f. in byte

with open("sample.txt", "w") as f:
    f.write("hello world")
    f.truncate(5)
with open('sample.txt', 'r') as f:
    print(f.read())

    # if i want that my file contains specition value of character I use .truncate() function





   