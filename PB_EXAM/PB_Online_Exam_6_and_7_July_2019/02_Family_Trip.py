budget_they_have = float(input())
nights_amount = int(input())
price_per_night = float(input())
extra_expenses = float(input())



if nights_amount > 7:
    price_per_night = price_per_night * 0.95


price_for_nights = price_per_night * nights_amount
extra_expenses1 = budget_they_have * (extra_expenses / 100)

total_amount = price_for_nights + extra_expenses1

if total_amount <= budget_they_have:
    diff = abs(total_amount - budget_they_have)
    print(f"Ivanovi will be left with {diff:.2f} leva after vacation.")
else:
    diff = abs(total_amount - budget_they_have)
    print(f"{diff:.2f} leva needed.")
