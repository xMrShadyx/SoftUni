import math
needed_hours = int(input())
needed_days = int(input())
workers = int(input())

days = needed_days * 0.9
hours = days * 8
overtime = workers * (2 * needed_days)
total_time = math.floor(hours + overtime)

if total_time >= needed_hours:
    diff = total_time - needed_hours
    print(f"Yes!{diff} hours left.")
else:
    diff = needed_hours - total_time
    print(f"Not enough time!{diff} hours needed.")


