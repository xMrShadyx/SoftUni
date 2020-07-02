temp = float(input())

if temp <= 0:
    print('unknown')
elif temp <= 11.9:
    print('Cold')
elif temp <= 14.9:
    print('Cool')
elif temp <= 20:
    print('Mild')
elif temp <= 25.9:
    print('Warm')
elif temp >= 26:
    print('Hot')