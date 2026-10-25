# dictonary are ordered collection of data items

dic = {
    334:"kunal",
    545:"raj",
    45:"jkkl",
}
print(dic[334])

# its used on rectangular bracket

info = {'name':'kunal','age':19,}
print(info)
print(info['name'])

# if we have to find out the value in the dictonary we use [] this bracket but we have to use dictonery with {} this bracket
# some if we have to find out the value with is not in the dictonary we use info.get but we use () braket not []

info = {'name':'kunal','age':19,}
print(info)
print(info.get('name2'))

# if we have to all value we use info.key

info = {'name':'kunal','age':19,}
print(info)
print(info.keys())
print(info.values())

for key in info.keys():
  print(f"The value to the key {key} is {info[key]}")
   


# Simple rule (remember this)
# Inside f-string:
# {variable} → print variable
# {something[index]} → get value

print(info.items())
for key,value in info.items():
   print(f"The value to the key {key} is {info[key]}")

#    With .items()
# for key, value in info.items():

# 👉 You directly get:

# key AND value together 
   