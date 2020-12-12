# count = int(input())
#
# synonyms = {}
#
#
# for _ in range(count):
# 	key = input()
# 	value = input()
# 	if key in synonyms:
# 		synonyms[key].append(value)
# 	else:
# 		synonyms[key] = []
# 		synonyms[key].append(value)
#
# for key, value in synonyms.items():
# 	print(f"{key} - {', '.join(value)}")

def read_count_lines(n):
	return [input() for _ in range(n)]


def get_words_with_synonyms(lines):
	word_synonyms_dict = {}
	n = len(lines)
	for i in range(0, n, 2):
		word = lines[i]
		synonyms = lines[i + 1]
		if word not in word_synonyms_dict:
			word_synonyms_dict[word] = []
		word_synonyms_dict[word].append(synonyms)
	return word_synonyms_dict


def print_words(word_synonyms_dict):
	for (word, synonyms) in word_synonyms_dict.items():
		print(f'{word} - {", ".join(synonyms)}')


def solve(lines):
	word_synonyms_dict = get_words_with_synonyms(lines)
	print_words(word_synonyms_dict)


# n = int(input())
# lines = read_count_lines(n * 2)

lines = ['cute', 'adorable', 'cute', 'charming', 'smart', 'clever']
solve(lines)
