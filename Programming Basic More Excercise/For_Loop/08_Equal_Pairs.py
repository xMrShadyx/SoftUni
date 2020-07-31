import sys
n = int(input())
num_sum = 0
num_sum_prev = 0
diff_max = -sys.maxsize
for i in range(n):
    num1 = int(input())
    num2 = int(input())
    num_sum = num1 + num2
    if num_sum != num_sum_prev:
        if i > 0:
            diff = abs(num_sum_prev - num_sum)
            if diff > diff_max:
                diff_max = diff
    num_sum_prev = num_sum
if diff_max == -sys.maxsize:
    print(f'Yes, value={num_sum}')
else:
    print(f'No, maxdiff={diff_max}')