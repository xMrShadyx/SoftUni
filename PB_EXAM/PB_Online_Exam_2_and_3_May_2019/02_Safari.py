budget = float(input())
gas = float(input())
day = input()

gas_price = gas * 2.1
total = gas_price + 100

if day == "Sunday":
    total = total * 0.8
else:
    total = total * 0.9

if budget > total:
    l_total = budget - total
    print(f"Safari time! Money left: {l_total:.2f} lv. ")
else:
    l_total = total - budget
    print(f"Not enough money! Money needed: {l_total:.2f} lv.")