wanted_profit = float(input())
cocktail_price = 0

user_input = input()
while user_input != 'Party!':
    cocktail_name = user_input
    number_of_cocktails = int(input())
    price = len(cocktail_name) * number_of_cocktails
    if price % 2 == 1:
        price -= price * 0.25
    cocktail_price += price
    if wanted_profit <= cocktail_price:
        break
    user_input = input()

result = wanted_profit - cocktail_price
if result > 0:
    print(f'We need {result:.2f} leva more.')
    print(f'Club income - {cocktail_price:.2f} leva.')
else:
    print('Target acquired.')
    print(f'Club income - {cocktail_price:.2f} leva.')

