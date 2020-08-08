n = int(input())

# for i in range(1, n + 1):
#     sum_of_digits = 0
#     for digit in str(i):
#         sum_of_digits += int(digit)
#
#     is_special = sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11
#
#     print(f'{i} -> {is_special}')
#
#
for number in range(1, n + 1):
    sum_of_digits = 0

    number_copy = number
    while number_copy > 0:
        digit = number_copy % 10
        sum_of_digits += digit
        number_copy = int(number_copy / 10)
#    is_special = sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11
    is_special = sum_of_digits in (5, 7, 11)
    print(f"{number} -> {is_special}")
