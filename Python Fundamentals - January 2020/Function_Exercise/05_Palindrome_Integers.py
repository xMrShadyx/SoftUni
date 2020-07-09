def is_palindrome(num_str):
    reversed_num = num_str[::-1]

    is_palindrome = True

    if num_str != reversed_num:
        is_palindrome = False
    return is_palindrome


text = input().split(', ')
for num in text:
    print(is_palindrome(num))
