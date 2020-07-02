#•	Бюджет на групата – цяло число;
# •	Сезон –  текст: "Spring", "Summer", "Autumn" или "Winter";
# •	Брой рибари – цяло число.

budget = int(input())
season = input()
fisherman = int(input())

boat_price = 0

if season == 'Spring':
    boat_price = 3000
elif season == 'Summer' or season == 'Autumn':
    boat_price = 4200
elif season == 'Winter':
    boat_price = 2600

if fisherman <= 6:
    boat_price *= 0.9
elif 7 <= fisherman <= 11:
    boat_price *= 0.85
elif fisherman > 12:
    boat_price *= 0.75

if fisherman % 2 == 0 and season != "Autumn":
    boat_price *= 0.95

if boat_price <= budget:
    money_left = abs(boat_price - budget)
    print(f'Yes! You have {money_left:.2f} leva left.')
else:
    money_left = abs(boat_price - budget)
    print(f'Not enough money! You need {money_left:.2f} leva.')
