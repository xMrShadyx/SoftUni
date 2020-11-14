count = int(input())

synonyms = {}


for _ in range(count):
	key = input()
	value = input()
	if key in synonyms:
		synonyms[key].append(value)
	else:
		synonyms[key] = []
		synonyms[key].append(value)

for key, value in synonyms.items():
	print(f"{key} - {', '.join(value)}")