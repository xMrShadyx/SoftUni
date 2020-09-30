gifts = input().split()

while True:
    word = input()
    token = word.split()

    if word == "No Money":
        break

    if "OutOfStock" == token[0]:
        for gift in gifts:

            if gift == token[1]:
                index = gifts.index(gift)
                gifts.pop(index)
                gifts.insert(index, "None")

    elif "Required" == token[0]:
        index = int(token[2])

        if 0 <= index <= len(gifts) - 1:
            gifts.pop(index)
            gifts.insert(index, token[1])

    elif "JustInCase" == token[0]:
        gifts.pop()
        gifts.append(token[1])

for gift in gifts:
    if gift == "None":
        gifts.remove("None")

print(f"{' '.join(gifts)}")