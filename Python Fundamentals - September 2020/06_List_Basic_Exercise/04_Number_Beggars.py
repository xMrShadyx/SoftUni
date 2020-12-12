numbers = input().split(', ')
beggars = int(input())
sums = [0] * beggars

while numbers:
	for beggar in range(beggars):
		if not numbers:
			break

		sums[beggar] += int(numbers.pop(0))

print(sums)