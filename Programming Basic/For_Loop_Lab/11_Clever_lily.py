n = int(input())
wm_price = float(input())
toy_price = int(input())

saved_money = 0
toys_amount = 0

for i in range(1, n+1):
    if i % 2 == 0:
        saved_money += i * 5
        saved_money -= 1
    if i % 2 != 0:
        toys_amount += 1 * toy_price

total = saved_money + toys_amount

if total >= wm_price:
    diff = total - wm_price
    print(f'Yes! {diff:.2f}')
else:
    diff = wm_price - total
    print(f"No! {diff:.2f}")