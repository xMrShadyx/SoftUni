string = input()

number = []
alpha = []
symbol = []

for item in string:
    if item.isdigit():
        number.append(item)
    elif item.isalpha():
        alpha.append(item)
    else:
        symbol.append(item)

print("".join(el for el in number))
print("".join(el for el in alpha))
print("".join(el for el in symbol))
