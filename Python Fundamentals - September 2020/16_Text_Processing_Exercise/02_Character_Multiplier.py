data = input().split()

data.sort(key=lambda x: len(x))
result = 0

for i in range(len(data[0])):
	result += ord(data[0][i]) * ord(data[1][i])

remainder = sum([ord(i) for i in data[1][len(data[0]):]])

print(f'{result + remainder}')