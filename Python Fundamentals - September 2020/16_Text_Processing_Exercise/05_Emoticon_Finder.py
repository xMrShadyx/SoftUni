import re
text = input()
#REG express > \b:.

for i in range(len(text)):
    if text[i] == ":":
        print(f"{text[i]}{text[i + 1]}")
