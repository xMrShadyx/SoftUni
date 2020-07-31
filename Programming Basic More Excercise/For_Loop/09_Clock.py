minutes = 0
hours = 0

while True:
    print(f'{hours} : {minutes}')
    minutes = minutes + 1
    if minutes == 60:
        minutes = 0
        hours = hours + 1
    if hours == 24:
        hours = 0
    if hours == 23 and minutes == 58 + 1:
        print(f'{hours} : {minutes}')
        break
