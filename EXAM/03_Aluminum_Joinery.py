amount_dogrami = int(input())
type_dogrami = input()
delivery_way = input()

price = 0
single_price = 0

is_valid = False

if type_dogrami == '90X130':
    single_price = 110
elif type_dogrami == '100X150':
    single_price = 140
elif type_dogrami == '130X180':
    single_price = 190
elif type_dogrami == '200X300':
    single_price = 250

if type_dogrami == '90X130':
    if 10 < amount_dogrami < 30:
        price = single_price * amount_dogrami
    elif amount_dogrami > 30 and amount_dogrami < 60:
        price = (single_price * 0.95) * amount_dogrami
    elif amount_dogrami > 60:
        price = (single_price * 0.92) * amount_dogrami
    else:
        is_valid = True
elif type_dogrami == '100X150':
    if 10 < amount_dogrami < 40:
        price = single_price * amount_dogrami
    elif amount_dogrami > 40 and amount_dogrami < 80:
        price = (single_price * 0.94) * amount_dogrami
    elif amount_dogrami > 80:
        price = (single_price * 0.90) * amount_dogrami
    else:
        is_valid = True
elif type_dogrami == '130X180':
    if 10 < amount_dogrami < 20:
        price = single_price * amount_dogrami
    elif amount_dogrami > 20 and amount_dogrami < 50:
        price = (single_price * 0.93) * amount_dogrami
    elif amount_dogrami > 50:
        price = (single_price * 0.88) * amount_dogrami
    else:
        is_valid = True
elif type_dogrami == '200X300':
    if 10 < amount_dogrami < 25:
        price = single_price * amount_dogrami
    elif amount_dogrami > 25 and amount_dogrami < 50:
        price = (single_price * 0.91) * amount_dogrami
    elif amount_dogrami > 50:
        price = (single_price * 0.86) * amount_dogrami
    else:
        is_valid = True

if delivery_way == 'With delivery':
    price += 60

if amount_dogrami >= 100:
    price = price * 0.96

if is_valid:
    print('Invalid order')
else:
    print(f"{price:.2f} BGN")