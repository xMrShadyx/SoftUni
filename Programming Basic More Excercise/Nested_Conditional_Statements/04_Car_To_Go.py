budget = float(input())
season = input()

class1 = ''
car = ''
price = 0

if budget <= 100:
    if season == 'Summer':
        class1 = 'Economy class'
        car = 'Cabrio'
        price = budget * 0.35
    elif season == 'Winter':
        class1 = 'Economy class'
        car = 'Jeep'
        price = budget * 0.65
elif 100 < budget <= 500:
    if season == 'Summer':
        class1 = 'Compact class'
        car = 'Cabrio'
        price = budget * 0.45
    elif season == 'Winter':
        class1 = 'Compact class'
        car = 'Jeep'
        price = budget * 0.80
elif budget > 500:
    if season == 'Summer':
        class1 = 'Luxury class'
        car = 'Jeep'
        price = budget * 0.90
    elif season == 'Winter':
        class1 = 'Luxury class'
        car = 'Jeep'
        price = budget * 0.90



print(f"{class1}")
print(f'{car} - {price:.2f}')
