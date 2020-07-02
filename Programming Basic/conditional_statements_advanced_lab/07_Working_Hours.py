time = int(input())
day = input()

if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday' or day == 'Saturday':
    if time >= 10 and time <=18:
        print('open')
    else:
        print('closed')
else:
    print('closed')