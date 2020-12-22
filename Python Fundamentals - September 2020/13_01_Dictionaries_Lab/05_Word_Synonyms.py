<<<<<<< HEAD
from collections import defaultdict

words_with_synonyms = defaultdict(list)

n = int(input())

for _ in range(n):
	word = input()
	synonym = input()
	words_with_synonyms[word].append(synonym)

for word, synonyms in words_with_synonyms.items():
=======
from collections import defaultdict

words_with_synonyms = defaultdict(list)

n = int(input())

for _ in range(n):
	word = input()
	synonym = input()
	words_with_synonyms[word].append(synonym)

for word, synonyms in words_with_synonyms.items():
>>>>>>> 06f2e621b68de7dbe64b4c1441e71917f616ece7
	print(f'{word} - {", ".join(synonyms)}')