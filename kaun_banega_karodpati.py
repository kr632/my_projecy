# we make kbc quiz in this phython script

questions = [["What is the capital of India?", "Delhi", "Mumbai", "Kolkata", "Chennai",1],
["What is the capital of USA?", "Washington DC", "New York", "Los Angeles", "Chicago",1],
["What is the capital of UK?", "London", "Manchester", "Birmingham", "Liverpool",2],
["Who is the president of India?", "Narendra Modi", "Rahul Gandhi", "Amit Shah", "Sonia Gandhi",1],]      

level = [1000, 5000, 10000, 50000]
money = 0
for i in range(0 ,len(questions)):
    question = questions [i]
    print(f"Question for Rs. {level[i]}")
    print(f"a. {question[1]}  b. {question[2]}")
    print(f"c. {question[3]}  d. {question[4]}")
    reply = int(input("Enter your answer (1-4): "))
    if reply == question[5]:
        print(f"Correct answer! You have won Rs. {level[i]}")
        if i == 1:
            money = 5000
        elif i == 2:
            money = 10000
        elif i == 3:
            money = 50000

    else:
        print("Wrong answer!")
        break
