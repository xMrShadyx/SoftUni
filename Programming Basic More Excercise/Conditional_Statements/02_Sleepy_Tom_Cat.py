days = int(input())

wdays = abs(days - 365) * 63
hdays = days * 127
totalhw = wdays + hdays

left_time = abs(30000 - totalhw)

hours = left_time // 60
mins = left_time % 60


if 30000 > totalhw:
    print('Tom sleeps well')
    print(f'{hours} hours and {mins} minutes less for play')
else:
    print('Tom will run away')
    print(f'{hours} hours and {mins} minutes more for play')

