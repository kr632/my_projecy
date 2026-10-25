# f = open("hey.txt", "r")
# while True:
#     line = f.readline()
#     if not line:
#         break
#     print(line.strip())

# f = open("hey.txt", "r")
# i = 0
# while True:
#     i = i + 1
#     line = f.readline()
#     if not line:
#         break
#     k1 = line.split(",")[0]
#     k2 = line.split(",")[1]
#     k3 = line.split(",")[2]
#     print(f"marks of student {i} is {int(k1)*2}")
#     print(f"marks of student {i} is {int(k2)*2}")
#     print(f"marks of student {i} is {int(k3)*2}")
#     print(line)

# writelines is used to write a list of string to a new file

# f = open("heykuna.txt", "w")
# lines = ["hello\n", "how are you\n", "i am fine\n"]
# f.writelines(lines)
# f.close()
# write create new file

f = open("heykunal.txt", "w")
lines = ["hellon", "how are youn", "i am finen"]
for line in lines:
    line = line + "\n"
f.writelines(lines)
f.close()



