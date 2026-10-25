f = open("hey.txt", "r")
print(f)
text = f.read()
print(text)
f.close()

#this is used to read the contents of a file.
#  We open the file in read mode ("r"), read its 
# contents, and then close the file to free up system resources.
#r mode is default for open() function, so we can omit it and just write open("dictionary.txt")

#writing to a file
f = open("hey.txt", "w")
f.write("Hello, this is a new line.\n")
f.close()

#if we use with statement, it will automatically close the file after the block of code is exe
# cuted, even if an error occurs. This is a best practice for handling files in Python.

with open("hey.txt", "w") as f:
    f.write("Hello, this is a new word.\n")

    # we have to use f.close to close the file