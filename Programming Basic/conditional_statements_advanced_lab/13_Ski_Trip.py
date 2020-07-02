days = int(input())
room_type = input()
rating = input()

nights = days - 1
price = 0

if room_type == "room for one person":
    price = nights * 18

elif room_type == 'apartment':
    price = nights * 25
    if days < 10:
        nprice = price * 0.30
        price = price - nprice
    elif 10 <= days <= 15:
        nprice = price * 0.35
        price = price - nprice
    elif days > 15:
        nprice = price * 0.50
        price = price - nprice

elif room_type == 'president apartment':
    price = nights * 35
    if days < 10:
        nprice = price * 0.10
        price = price - nprice
    elif 10 <= days <= 15:
        nprice = price * 0.15
        price = price - nprice
    elif days > 15:
        nprice = price * 0.20
        price = price - nprice


if rating == 'positive':
    pprice = price * 0.25
    price = pprice + price
elif rating == 'negative':
    pricen = price * 0.1
    price = abs(pricen - price)

print(f'{price:.2f}')
