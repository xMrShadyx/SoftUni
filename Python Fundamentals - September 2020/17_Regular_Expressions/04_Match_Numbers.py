import re
pattern = r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))"
text = input()
matches = re.finditer(pattern, text)

for match in matches:
    print(match.group(0), end=' ')
