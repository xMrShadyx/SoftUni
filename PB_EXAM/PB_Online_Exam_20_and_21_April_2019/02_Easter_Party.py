amount_of_guests = int(input())
coverts_price = float(input())
budget = float(input())

price = 0

if 10 <= amount_of_guests <= 15:
    price = coverts_price * 0.85
elif 15 <= amount_of_guests <= 20:
    price = coverts_price * 0.80
elif amount_of_guests > 20:
    price = coverts_price * 0.75

cake_price = budget / 10

if price != 0:
    total = (price * amount_of_guests) + cake_price
else:
    total = (coverts_price * amount_of_guests) + cake_price

if total > budget:
    diff = total - budget
    print(f"No party! {diff:.2f} leva needed.")
else:
    diff = budget - total
    print(f"It is party time! {diff:.2f} leva left.")
