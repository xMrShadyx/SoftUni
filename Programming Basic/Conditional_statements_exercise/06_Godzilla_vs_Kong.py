# Ред 1.	Бюджет за филма – реално число в интервала [1.00 … 1000000.00]
# Ред 2.	Брой на статистите – цяло число в интервала [1 … 500]
# Ред 3.	Цена за облекло на един статист – реално число в интервала [1.00 … 1000.00]
movie_budget = float(input())
amount_statist = float(input())
price_amount = float(input())

# •	Декорът за филма е на стойност 10% от бюджета.
movie_decor = movie_budget * 0.1

# •	При повече от 150 статиста,  има отстъпка за облеклото на стойност 10%.
if amount_statist > 150:
    discount = price_amount * 0.1
    last_discount = price_amount - discount
    price_amount = price_amount - discount


# Изход
# На конзолата трябва да се отпечатат два реда:
suma_za_oblekloto = amount_statist * price_amount
obshta_sumana_filma = movie_decor + suma_za_oblekloto
kraina_suma = movie_budget - obshta_sumana_filma

kraina_suma = abs(kraina_suma)

# •	Ако парите за декора и дрехите са по малко или равни на бюджета:
# o	"Action!"
# o	"Wingard starts filming with {останалите пари} leva left."
if obshta_sumana_filma <= movie_budget:
    print('Action!')
    print(f'Wingard starts filming with {kraina_suma:.2f} leva left.')

# •	Ако  парите за декора и дрехите са повече от бюджета:
# o	"Not enough money!"
# o	"Wingard needs {парите недостигащи за филма} leva more."
else:
    print('Not enough money!')
    print(f'Wingard needs {kraina_suma:.2f} leva more.')

