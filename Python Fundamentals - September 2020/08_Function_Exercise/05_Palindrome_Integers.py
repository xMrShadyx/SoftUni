n = input().split(", ")


def palindrome(n_list):
    k = ''
    for i in n_list:
        k = (str(i)[::-1])
        if str(i) != str(k):
            print('False')
        else:
            print('True')


palindrome(n)
