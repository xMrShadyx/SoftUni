width = int(input())
length = int(input())
height = int(input())

size = width * length * height

command = input()

while command != "Done":
    size -= int(command)

    if size <= 0:
        break

    command = input()

if size > 0:
    print(f"{size} Cubic meters left.")
else:
    print(f"No more free space! You need {abs(size)} Cubic meters more.")
