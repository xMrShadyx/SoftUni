import re

pattern = re.compile(r"""
                         ((?<=^_)|(?<=\s_))   # Look ahead
                         [A-Za-z0-9]+\b   # From A-Za-z0-9 etc..
                         """, re.VERBOSE)

data = input()
result = [el.group() for el in re.finditer(pattern, data)]
print(",".join(result))
