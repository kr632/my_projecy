def func1():
      try:
          l = [1,2,3,4,4]
          i = int(input("enter your name"))
          print(l[i])
          return 1
      except: 
        print("some error occured")
        return 0
      
      finally:
        print("i am also executed")

x = func1()
print()

    # finally is used to run the code whether its contain wrong value 

