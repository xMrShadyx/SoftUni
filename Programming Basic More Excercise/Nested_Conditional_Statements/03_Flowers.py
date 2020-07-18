amount_chrysanthemum = int(input())
amount_roses = int(input())
amount_tulips = int(input())
season = input()
is_holiday = input()

# seasons -> spring, summer, Аutumn, winter
price_chrysanthemum = 0
price_roses = 0
price_tulips = 0

total_flowers = amount_chrysanthemum + amount_roses + amount_tulips

if season == 'Spring' or season == 'Summer':
    price_chrysanthemum = amount_chrysanthemum * 2
    price_roses = amount_roses * 4.1
    price_tulips = amount_tulips * 2.5
elif season == 'Autumn' or 'Winter':
    price_chrysanthemum = amount_chrysanthemum * 3.75
    price_roses = amount_roses * 4.5
    price_tulips = amount_tulips * 4.15
total_flowers_price = price_chrysanthemum + price_roses + price_tulips

if is_holiday == 'Y':
    total_flowers_price += total_flowers_price * 0.15

if amount_roses >= 10 and season == 'Winter':
    total_flowers_price -= total_flowers_price * 0.10

if amount_tulips >= 7 and season == 'Spring':
    total_flowers_price -= total_flowers_price * 0.05

if total_flowers > 20:
    total_flowers_price -= total_flowers_price * 0.20

print(f"{total_flowers_price + 2:.2f}")
