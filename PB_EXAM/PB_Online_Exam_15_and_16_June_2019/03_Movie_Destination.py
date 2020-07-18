movie_budget = float(input())
destination = input()
season = input()
amount_days = int(input())

price = 0

if season == 'Winter':
    if destination == 'Dubai':
        price = 45000
    elif destination == 'Sofia':
        price = 17000
    elif destination == 'London':
        price = 24000
        
if season == 'Summer':
    if destination == 'Dubai':
        price = 40000
    elif destination == 'Sofia':
        price = 12500
    elif destination == 'London':
        price = 20250

total_price = amount_days * price

if destination == 'Sofia':
    total_price = (total_price * 0.25) + total_price

if destination == 'Dubai':
    total_price = total_price - (total_price * 0.30)


if total_price <= movie_budget:
    diff = abs(total_price - movie_budget)
    print(f"The budget for the movie is enough! We have {diff:.2f} leva left!")
else:
    diff1 = abs(movie_budget - total_price)
    print(f"The director needs {diff1:.2f} leva more!")
