n = int(input())

for number in range(1, n + 1):
    sum_of_digits = 0

    number_copy = number
    while number_copy > 0:
        digit = number_copy % 10
        sum_of_digits += digit
        number_copy = int(number_copy / 10)
    is_special = sum_of_digits in (5, 7, 11)
    print(f"{number} -> {is_special}")
