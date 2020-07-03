fx_rate = {
    'USD': 1.13,
    'BGN': 2.35,
    'RUB': 42.1,
 }


pounds_amount = float(input('Please enter amount in pounds: '))
print('Type of Currency available, USD, BGN, RUB')
target_currency = input('Please enter target currency: ')

pounds_fx_to_currency = fx_rate[target_currency]
amount_in_currency = pounds_amount * pounds_fx_to_currency

print('{:.2f} {}'.format(amount_in_currency,target_currency))