import re

text = input()
pattern = r"(^|(?<=\s))[a-z0-9]+[\._-]?[a-z0-9]+@[a-z]+\-?[a-z]+(\.[a-z]+\-?[a-z]+)+"

result = re.finditer(pattern, text, re.IGNORECASE)

for i in result:
    print(i.group())
