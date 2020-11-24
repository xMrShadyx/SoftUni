line = input()
total_power = 0
index = 0

while index < len(line):

    if line[index] == ">":
        total_power += int(line[index + 1])

    else:
        if total_power > 0:
            line = line[:index] + line[index + 1:]
            total_power -= 1
            continue

    index += 1

print(line)
