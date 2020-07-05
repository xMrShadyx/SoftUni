import sys

command = input()

min = sys.maxsize

while command != "Stop":
    number = int(command)

    if number < min:
        min = number

    command = input()

print(min)