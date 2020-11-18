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
