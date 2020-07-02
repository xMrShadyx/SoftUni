flower_type = input()
flower_amount = float(input())
budget = float(input())

price = 0

if flower_type == 'Roses':
    price = 5
    if flower_amount > 80:
        price *= 0.90

if flower_type == 'Dahlias':
    price = 3.8
    if flower_amount > 90:
        price *= 0.85

if flower_type == 'Tulips':
    price = 2.8
    if flower_amount > 80:
        price *= 0.85

if flower_type == 'Narcissus':
    price = 3
    if flower_amount < 120:
        price += price * 0.15

if flower_type == 'Gladiolus':
    price = 2.5
    if flower_amount < 80:
        price += price * 0.20

total = price * flower_amount


if budget >= total:
    total1 = budget - total
    print(f'Hey, you have a great garden with {flower_amount:.0f} {flower_type} and {total1:.2f} leva left.')
else:
    total1 = total - budget
    print(f'Not enough money, you need {total1:.2f} leva more.')

