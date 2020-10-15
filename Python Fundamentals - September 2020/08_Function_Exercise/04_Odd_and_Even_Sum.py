n1 = input()


def odd_even(n):
    odd = 0
    even = 0
    for i in n:
        if int(i) % 2 != 0:
            odd += int(i)
        else:
            even += int(i)
    return 'Odd sum = {}, Even sum = {}'.format(odd, even)


print(odd_even(n1))
