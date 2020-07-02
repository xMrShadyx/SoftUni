fruit = input()
day_week = input()
amount = float(input())

all_is_valid = True

price = 0

if day_week == 'Monday' or day_week == 'Tuesday' or day_week == 'Wednesday'\
        or day_week == 'Thursday' or day_week == 'Friday':
    if fruit == 'banana':
        price = 2.5
    elif fruit == 'apple':
        price = 1.2
    elif fruit == 'orange':
        price = 0.85
    elif fruit == 'grapefruit':
        price = 1.45
    elif fruit == 'kiwi':
        price = 2.7
    elif fruit == 'pineapple':
        price = 5.5
    elif fruit == 'grapes':
        price = 3.85
    else:
        all_is_valid = False
        print('error')
elif day_week == 'Saturday' or day_week == 'Sunday':
    if fruit == 'banana':
        price = 2.7
    elif fruit == 'apple':
        price = 1.25
    elif fruit == 'orange':
        price = 0.9
    elif fruit == 'grapefruit':
        price = 1.6
    elif fruit == 'kiwi':
        price = 3
    elif fruit == 'pineapple':
        price = 5.6
    elif fruit == 'grapes':
        price = 4.2
    else:
        all_is_valid = False
        print('error')
else:
    all_is_valid = False
    print('error')


total = price * amount

if all_is_valid:
    print(f'{total:.2f}')