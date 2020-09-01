budget = float(input())


cmd = input()
amount = 0
l_price = 0
total_items = 0

while cmd != "Stop":
    item = str(cmd)
    price = float(input())
    amount += 1
    total_items += 1
    if amount == 3:
        price /= 2
        amount = 0
        l_price += price
    else:
        l_price += price

    if l_price > budget:
        break

    cmd = input()

if l_price > budget:
    diff = l_price - budget
    print("You don't have enough money!")
    print(f"You need {diff:.2f} leva!")
else:
    print(f"You bought {total_items} products for {l_price:.2f} leva.")