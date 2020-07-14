city_name = input()  # ("Bansko",  "Borovets", "Varna" или "Burgas")
extras = input()  # ("noEquipment",  "withEquipment", "noBreakfast" или "withBreakfast")
vip_owning = input()  # ("yes" или "no")
amount_days = int(input())

price = 0
is_invalid = False

if city_name == 'Bansko' or city_name == 'Borovets':
    if extras == 'withEquipment':
        price = 100
        if vip_owning == 'yes':
            price = price * 0.90
    elif extras == 'noEquipment':
        price = 80
        if vip_owning == 'yes':
            price = price * 0.95
    else:
        is_invalid = True

elif city_name == 'Varna' or city_name == 'Burgas':
    if extras == 'withBreakfast':
        price = 130
        if vip_owning == 'yes':
            price = price * 0.88
    elif extras == 'noBreakfast':
        price = 100
        if vip_owning == 'yes':
            price = price * 0.93
    else:
        is_invalid = True
else:
    is_invalid = True

if amount_days > 7:
    amount_days = amount_days - 1

total = amount_days * price

if is_invalid:
    print("Invalid input!")
elif amount_days < 1:
    print("Days must be positive number!")
else:
    print(f"The price is {total:.2f}lv! Have a nice time!")

# Test #6 (Incorrect answer)
# Time used: 0.009 s
# Memory used: 8.36 MB
# Points: 87/100
