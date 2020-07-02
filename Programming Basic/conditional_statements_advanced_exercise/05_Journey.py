budget = float(input())
season = input()

type_holiday = ""
destination = ""

price = 0

if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        price = budget * 0.3
    else:
        price = budget * 0.7
elif 100 < budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        price = budget * 0.4
    else:
        price = budget * 0.8
elif budget > 1000:
    destination = 'Europe'
    price = budget * 0.9

if season == 'summer' and destination != "Europe":
    type_holiday = "Camp"
else:
    type_holiday = 'Hotel'

print(f'Somewhere in {destination}')
print(f'{type_holiday} - {price:.2f}')