start_hour = int(input())
start_minutes = int(input())

time_in_minutes = start_hour * 60 + start_minutes
time_plus_15_minutes = time_in_minutes + 15

final_hour = time_plus_15_minutes // 60
fina_minutes = time_plus_15_minutes % 60

if final_hour > 23:
    final_hour = final_hour - 24
if fina_minutes < 10:
    print(f'{final_hour}:0{fina_minutes}')
else:
    print(f'{final_hour}:{fina_minutes}')