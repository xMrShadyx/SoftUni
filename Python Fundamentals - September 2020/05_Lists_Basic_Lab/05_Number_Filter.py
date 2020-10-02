n = int(input())

even = []
odd = []
negative = []
positive = []

for i in range(n):
    numbers = int(input())
    if numbers % 2 == 0:
        even.append(numbers)
    if not numbers % 2 == 0:
        odd.append(numbers)
    if numbers < 0:
        negative.append(numbers)
    else:
        positive.append(numbers)

command = input()

if command == 'even':
    print(even)
elif command == 'odd':
    print(odd)
elif command == 'negative':
    print(negative)
elif command == 'positive':
    print(positive)
