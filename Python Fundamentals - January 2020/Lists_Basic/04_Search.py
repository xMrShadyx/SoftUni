n = int(input())
word = input()

strings = []
for _ in range(n):
    strings.append(input())

print(strings)
print([string for string in strings if word in string])
