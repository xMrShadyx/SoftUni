import re
line = input()

pattern = r"\d+"
numbers = []

while line:
    match = re.findall(pattern, line)
    if match:
        numbers.extend(match)
    line = input()
print(*numbers, sep=" ")
