drink = input()
extras = input()
amount = int(input())

price = 0

if drink == 'Espresso':
    if extras == 'Without':
        price = 0.90
    elif extras == 'Normal':
        price = 1
    elif extras == 'Extra':
        price = 1.2
elif drink == 'Cappuccino':
    if extras == 'Without':
        price = 1
    elif extras == 'Normal':
        price = 1.2
    elif extras == 'Extra':
        price = 1.6
elif drink == 'Tea':
    if extras == 'Without':
        price = 0.5
    elif extras == 'Normal':
        price = 0.6
    elif extras == 'Extra':
        price = 0.7

drink_amount = price * amount
if extras == 'Without':
    drink_amount = drink_amount * 0.65
if drink == 'Espresso' and amount > 5:
    drink_amount = drink_amount * 0.75
if drink_amount > 15:
    drink_amount = drink_amount * 0.8

print(f"You bought {amount} cups of {drink} for {drink_amount:.2f} lv.")
