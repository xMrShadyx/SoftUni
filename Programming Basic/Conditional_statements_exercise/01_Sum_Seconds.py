import math

time_first = float(input())
time_second = float(input())
time_third = float(input())

total_time = time_first + time_second + time_third

minutes = total_time / 60
seconds = total_time % 60

minutes = math.floor(minutes)
seconds = round(seconds)

if seconds < 10:
    print(f'{minutes}:0{seconds}')
else:
    print(f'{minutes}:{seconds}')