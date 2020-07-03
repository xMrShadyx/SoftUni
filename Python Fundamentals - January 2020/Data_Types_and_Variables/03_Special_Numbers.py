n = int(input())

for i in range(1, n + 1):
    sum_of_digits = 0
    for digit in str(i):
        sum_of_digits += int(digit)

    is_special = sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11

    print(f'{i} -> {is_special}')