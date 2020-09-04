line = input()
result = 0
student = 0
kid = 0
standard = 0
while line != "Finish":
    name = line
    free_place = int(input())
    command = input()

    total = 0

    while command != "End":
        ticket = command
        total += 1
        if ticket == "student":
            student += 1
        elif ticket == "standard":
            standard += 1
        elif ticket == "kid":
            kid += 1

        if total >= free_place:
            break

        command = input()
    result += total

    if command == "End" or total >= free_place:
        rest = free_place - total
        per = 100 - (rest / free_place * 100)
        print(f"{name} - {per:.2f}% full.")

    line = input()
if line == "Finish":
    print(f"Total tickets: {result}")
    print(f"{student / result * 100:.2f}% student tickets.")
    print(f"{standard / result * 100:.2f}% standard tickets.")
    print(f"{kid / result * 100:.2f}% kids tickets.")