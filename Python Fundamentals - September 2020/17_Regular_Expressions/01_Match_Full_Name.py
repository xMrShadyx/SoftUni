import re

data = input()

reg = r"\b[A-Z][a-z]+\s[A-Z][a-z]+\b"
names = re.findall(reg, data)

print(" ".join(names))
