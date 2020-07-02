import sys

n = int(input())

sum = 0
max = -sys.maxsize

for i in range(0, n):
    numbers = int(input())
    sum += numbers

    if numbers > max:
        max = numbers

sum -= max

if sum == max:
    print(f'Yes\nSum = {sum}')
else:
    print(f'No\nDiff = {abs(max - sum)}')