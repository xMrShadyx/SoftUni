import sys

command = input()

max = -sys.maxsize

while command != "Stop":
    number = int(command)

    if number > max:
        max = number

    command = input()

print(max)