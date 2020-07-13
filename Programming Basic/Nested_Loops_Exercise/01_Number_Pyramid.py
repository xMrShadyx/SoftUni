n = int(input())
number = 1
flag = False

for i in range(1, n + 1):
    output = ""
    for row in range(1, i +1):
        output += str(number) + " "
        if number == n:
            flag = True
            break
        number += 1
    print(output)
    if flag:
        break


