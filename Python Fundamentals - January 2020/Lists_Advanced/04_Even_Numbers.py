numbers = map(int, input().split(', '))
print([index for index, number in enumerate(numbers) if number % 2 == 0])
