certain_period = int(input())

doctors = 7

day = 0
non_checked = 0
checked = 0
for i in range(certain_period):
    days = int(input())
    day += 1
    if day % 3 == 0 and non_checked > checked:
        doctors += 1

    if doctors >= days:
        checked += days
    else:
        non_checked += days - doctors
        checked += doctors

print(f'Treated patients: {checked}.')
print(f'Untreated patients: {non_checked}.')