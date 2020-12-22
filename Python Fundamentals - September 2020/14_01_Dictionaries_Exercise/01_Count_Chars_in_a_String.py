<<<<<<< HEAD
strings = input()
dict = {}

for a in strings:
    if not a == " ":
        if not a in dict:
            dict[a] = 0
        dict[a] += 1

for key,value in dict.items():
    print(f"{key} -> {value}")
=======
strings = input()
dict = {}

for a in strings:
    if not a == " ":
        if not a in dict:
            dict[a] = 0
        dict[a] += 1

for key,value in dict.items():
    print(f"{key} -> {value}")
>>>>>>> 06f2e621b68de7dbe64b4c1441e71917f616ece7
