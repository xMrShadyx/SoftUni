from collections import defaultdict

words_with_synonyms = defaultdict(list)

n = int(input())

for _ in range(n):
	word = input()
	synonym = input()
	words_with_synonyms[word].append(synonym)

for word, synonyms in words_with_synonyms.items():
	print(f'{word} - {", ".join(synonyms)}')