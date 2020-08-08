number_range = int(input())

search_word = input()
strings = []
filtered_strings = []

for _ in range(number_range):
    string = input()
    strings.append(string)

for string in strings:
    if search_word in string:
        filtered_strings.append(string)

print(strings)
print(filtered_strings)
