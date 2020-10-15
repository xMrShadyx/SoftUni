def char_in_range(val1, val2):
    for i in range(ord(val1) + 1, ord(val2)):
        print(chr(i), end=" ")


num1 = input()
num2 = input()
char_in_range(num1, num2)
