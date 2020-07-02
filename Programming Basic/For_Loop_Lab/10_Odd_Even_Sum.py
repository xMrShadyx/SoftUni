n = int(input())

even_sum = 0
odd_sum = 0

for i in range(1, n+1):
    num = int(input())
    if i % 2 == 0:
        even_sum += num
    else:
        odd_sum += num

if even_sum == odd_sum:
    print(f'Yes \nSum = {even_sum}')
else:
    diff = abs(even_sum - odd_sum)
    print(f'No \nDiff = {diff}')
