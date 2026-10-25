# you cant change a tuple , but you can change the list list is used like [] and tuple like ()
# when we find out number number like which place we find that number so we use [] and we call it indexing example marks[0]
# and we can also find out the range of number like marks[1:6] and we can also find out the range of number with step like marks[1:6:3]

tupple = (1,2,3,4,5)
print(tupple[0])

# if we have to cheak that number or integer present in the tuple we use if statement like this example

tupple = (1,2,3,4,5)
print(tupple[0])

if 1 in tupple:
    print("number is present in the tuple")

    # when we do slicing it creates a new tuple and the original tuple remains unchanged

    tupple1 = tupple[1:3]
    print(tupple1)

    
