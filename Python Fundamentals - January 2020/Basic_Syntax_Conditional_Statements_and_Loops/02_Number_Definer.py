n = float(input())

if n == 0:
    print('zero')
else:
    if abs(n) < 1:
        print('small', end=' ')
    elif abs(n) > 1_000_000:
        print('large', end=' ')
    if n > 0:
        print('positive')
    elif n < 0:
        print('negative')
