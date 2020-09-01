contract_period = input() #one/two
contract_type = input() #"Small",  "Middle", "Large"или "ExtraLarge"
mob_internet = input() #"yes" или "no"
amount_months = int(input()) # 1 ~ 12

price = 0

if contract_period == "one":
    if contract_type == "Small":
        price = 9.98
    elif contract_type == "Middle":
        price = 18.99
    elif contract_type == "Large":
        price = 25.98
    elif contract_type == "ExtraLarge":
        price = 35.99
elif contract_period == "two":
    if contract_type == "Small":
        price = 8.58
    elif contract_type == "Middle":
        price = 17.09
    elif contract_type == "Large":
        price = 23.59
    elif contract_type == "ExtraLarge":
        price = 31.79

if mob_internet == "yes":
    if price <= 10:
        price += 5.5
    elif price <= 30:
        price += 4.35
    elif price > 30:
        price += 3.85

months_to_pay = price * amount_months
if contract_period == "two":
    months_to_pay = months_to_pay * 0.9625

print(f"{months_to_pay:.2f} lv.")