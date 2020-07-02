exam_hour = int(input())
exam_mins = int(input())
arrival_hour = int(input())
arrival_mins = int(input())

exam_total_mins = exam_hour * 60 + exam_mins
arrival_total_mins = arrival_hour * 60 + arrival_mins

if exam_total_mins - 30 <= arrival_total_mins <= exam_total_mins:
    print("On time")
    if exam_total_mins != arrival_total_mins:
        diff = exam_total_mins - arrival_total_mins
        print(f'{diff} minutes before the start')
elif arrival_total_mins < exam_total_mins - 30:
    print('Early')
    diff = exam_total_mins - arrival_total_mins
    if diff < 60:
        print(f'{diff} minutes before the start')
    else:
        diff_hour = diff // 60
        diff_mins = diff % 60
        if diff_mins < 10:
            print(f'{diff_hour}:0{diff_mins} hours before the start')
        else:
            print(f'{diff_hour}:{diff_mins} hours before the start')
else:
    print('Late')
    diff = arrival_total_mins - exam_total_mins
    if diff < 60:
        print(f'{diff} minutes after the start')
    else:
        diff_hour = diff // 60
        diff_mins = diff % 60
        if diff_mins < 10:
            print(f'{diff_hour}:0{diff_mins} hours after the start')
        else:
            print(f'{diff_hour}:{diff_mins} hours after the start')