strings = input()
dict = {}

for a in strings:
    if not a == " ":
        if not a in dict:
            dict[a] = 0
        dict[a] += 1

for key,value in dict.items():
    print(f"{key} -> {value}")
