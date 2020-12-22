<<<<<<< HEAD
line = input()
dict = {}
while line != "stop":
    type = line
    quantity = int(input())
    if not type in dict:
        dict[type] = quantity
    else:
        dict[type]  += quantity

    line = input()

for key,value in dict.items():
    print(f"{key} -> {value}")
=======
line = input()
dict = {}
while line != "stop":
    type = line
    quantity = int(input())
    if not type in dict:
        dict[type] = quantity
    else:
        dict[type]  += quantity

    line = input()

for key,value in dict.items():
    print(f"{key} -> {value}")
>>>>>>> 06f2e621b68de7dbe64b4c1441e71917f616ece7
