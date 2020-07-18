budget = float(input())
season = input()

location = ''
price = 0
place = ''

if budget <= 1000:
    location = 'Camp'
    if season == 'Summer':
        place = 'Alaska'
        price = budget * 0.65
    elif season == 'Winter':
        place = 'Morocco'
        price = budget * 0.45
elif 1000 < budget <= 3000:
    location = 'Hut'
    if season == 'Summer':
        place = 'Alaska'
        price = budget * 0.80
    elif season == 'Winter':
        place = 'Morocco'
        price = budget * 0.60
elif budget > 3000:
    location = 'Hotel'
    if season == 'Summer':
        place = 'Alaska'
        price = budget * 0.9
    elif season == 'Winter':
        place = 'Morocco'
        price = budget * 0.9
        
print(f'{place} - {location} - {price:.2f}')
    