words = input().split()

occurrences = {}

words = [w.lower() for w in words]

for word in words:
	occurrences[word] = words.count(word)

for key, value in occurrences.items():
	if value % 2 != 0:
		print(key, end=' ')