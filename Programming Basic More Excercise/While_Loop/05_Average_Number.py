n = int(input())

numbers = 0
for i in range(n):
    number = int(input())
    numbers += number

print(f"{numbers / n:.2f}")
