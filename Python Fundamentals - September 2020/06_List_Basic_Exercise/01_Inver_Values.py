insert = input().split()
first_string = insert

new_string = []

for x in first_string:
    if int(x) < 0:
        new_string.append(abs(int(x)))
    else:
        new_string.append(int(x) * -1)

print(new_string)