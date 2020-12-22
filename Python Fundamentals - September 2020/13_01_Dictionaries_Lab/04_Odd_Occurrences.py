<<<<<<< HEAD
from collections import defaultdict


occurrences = defaultdict(int)
words = [w.lower() for w in input().split(' ')]

for word in words:
	occurrences[word] += 1

filtered_item_words = filter(lambda item: item[1] % 2 != 0, occurrences.items())
print(' '.join(list([item[0] for item in filtered_item_words])))
=======
from collections import defaultdict


occurrences = defaultdict(int)
words = [w.lower() for w in input().split(' ')]

for word in words:
	occurrences[word] += 1

filtered_item_words = filter(lambda item: item[1] % 2 != 0, occurrences.items())
print(' '.join(list([item[0] for item in filtered_item_words])))
>>>>>>> 06f2e621b68de7dbe64b4c1441e71917f616ece7
