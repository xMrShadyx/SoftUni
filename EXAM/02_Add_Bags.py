price_for_20_kilos = float(input())
bagaj_kilos = float(input())
day_to_travel = int(input())
amount_bagaji = int(input())

price = 0

if bagaj_kilos < 10:
    price = price_for_20_kilos * 0.2
elif 10 <= bagaj_kilos <= 20:
    price = price_for_20_kilos * 0.5
else:
    price = price_for_20_kilos

if day_to_travel < 7:
    price += price * 0.4
elif 7 <= day_to_travel <= 30:
    price += price * 0.15
else:
    price += price * 0.1

print(f" The total price of bags is: {price * amount_bagaji:.2f} lv. ")