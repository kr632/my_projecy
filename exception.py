# exception handling 

# if we have to run the table

# a = input("enter you numnber")
# try:
#     for i in range (1,11):
#         print(f"{int(a)} x {i} = {int(a)*i}")
# # except Exception as e:
# #     print(e)
# except:
#     print("invalid input")

    # its basically soved the errors in phython for user input
    
try:
    num = int(input("Enter number: "))
    a = [4,4,5]
    print(a[num])
except ValueError:
    print("Please enter a valid number")
except IndexError:
    print("index error")

    example

    def withdraw(amount):
    if amount > 1000:
        raise ValueError("Limit exceeded")   

try:
    withdraw(int(input("Enter amount to withdraw: ")))
except ValueError as e:
    print("Transaction failed:", e) 
else:
    print("Transaction successful")


