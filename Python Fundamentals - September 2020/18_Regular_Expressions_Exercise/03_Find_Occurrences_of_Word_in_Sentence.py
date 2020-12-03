import re
search = input()
searched_word = input()

pattern = re.compile(f"\\b{searched_word}\\b", re.IGNORECASE)
result = re.findall(pattern, search)
print(len(result))
