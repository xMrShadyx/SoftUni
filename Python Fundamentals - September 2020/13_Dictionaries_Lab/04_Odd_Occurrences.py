# words = input().split()
#
# occurrences = {}
#
# words = [w.lower() for w in words]
#
# for word in words:
# 	occurrences[word] = words.count(word)
#
# for key, value in occurrences.items():
# 	if value % 2 != 0:
# 		print(key, end=' ')

def count_occurrences(words):
	words_occurrences = {}
	for word in words:
		if word not in words_occurrences:
			words_occurrences[word] = 0
		words_occurrences[word] += 1
	return words_occurrences


def get_words_with_odd_occurrences(words_occurrences):
	return [word for (word, count) in words_occurrences.items() if count % 2 == 1]


def solve(words_str):
	words = [word.lower() for word in words_str.split(' ')]
	words_occurrences = count_occurrences(words)
	odd_words = get_words_with_odd_occurrences(words_occurrences)
	print(' '.join(odd_words))


solve(input())

# tests = [
# 	'Java C# PHP PHP JAVA C java',
# 	'3 5 5 hi pi HO Hi 5 ho 3 hi pi',
# 	'a a A SQL xx a xx a A a XX c',
# ]
#
# [solve(test) for test in tests]
