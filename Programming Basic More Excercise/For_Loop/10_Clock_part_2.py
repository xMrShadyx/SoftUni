seconds = 0
minutes = 0
hours = 0

while True:
    print(f'{hours} : {minutes} : {seconds}')
    seconds = seconds + 1
    if seconds == 60:
        seconds = 0
        minutes = minutes + 1
    if minutes == 60:
        minutes = 0
        hours = hours + 1
    if hours == 24:
        hours = 0
    if hours == 23 and minutes == 59 and seconds == 59:
        print(f'{hours} : {minutes} : {seconds}')
        break
