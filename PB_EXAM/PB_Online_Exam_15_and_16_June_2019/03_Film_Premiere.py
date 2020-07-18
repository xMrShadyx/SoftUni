the_movie = input()
food_for_movie = input()
tickets = int(input())

price = 0

if the_movie == 'John Wick':
    if food_for_movie == 'Drink':
        price = 12
    elif food_for_movie == 'Popcorn':
        price = 15
    elif food_for_movie == 'Menu':
        price = 19
    total = tickets * price
    print(f'Your bill is {total:.2f} leva.')

if the_movie == 'Star Wars':
    if food_for_movie == 'Drink':
        price = 18
    elif food_for_movie == 'Popcorn':
        price = 25
    elif food_for_movie == 'Menu':
        price = 30
    if tickets >= 4:
        total = (tickets * price) * 0.70
        print(f'Your bill is {total:.2f} leva.')
    else:
        total = tickets * price
        print(f'Your bill is {total:.2f} leva.')

if the_movie == 'Jumanji':
    if food_for_movie == 'Drink':
        price = 9
    elif food_for_movie == 'Popcorn':
        price = 11
    elif food_for_movie == 'Menu':
        price = 14
    if tickets == 2:
        total = (tickets * price) * 0.85
        print(f'Your bill is {total:.2f} leva.')
    else:
        total = tickets * price
        print(f'Your bill is {total:.2f} leva.')