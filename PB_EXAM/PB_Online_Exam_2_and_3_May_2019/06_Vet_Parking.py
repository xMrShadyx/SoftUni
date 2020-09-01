amount_days = int(input())
amount_hours = int(input())
price = 0
total_price = 0

for i in range(amount_days):
    price = 0
    for k in range(amount_hours):
        if i % 2 == 0 and k % 2 != 0:
            price += 1.25
            total_price += 1.25
        elif i % 2 != 0 and k % 2 == 0:
            price += 2.5
            total_price += 2.5
        else:
            price += 1
            total_price += 1
    print(f"Day: {i + 1} - {price:.2f} leva")
