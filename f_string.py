# formating is use in phython by .format like

hey = "my name is {} and I belongs to {}"

country = "INDIA"
name = "kunal"

# for using f string we have to use f in print statement

print(hey.format(name,country))
print(f"hey my name is {name} and I am from {country}")

# we can also use f string for using in only 2 or 3 decimal in points

price = 1.265454
txt = f"for only {price:.3f}"
print (txt)

we use curly bracket in this