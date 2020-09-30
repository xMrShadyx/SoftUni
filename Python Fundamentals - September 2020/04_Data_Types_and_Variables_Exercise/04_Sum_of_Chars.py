n = int(input())
result = 0

for i in range(n):
    numbers = input()
    result += ord(numbers)

print(f"The sum equals: {result}")
