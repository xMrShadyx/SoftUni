price_kilo_vege = float(input())
price_kilo_fruit = float(input())
total_vege_kilo = float(input())
total_fruit_kilo = float(input())

euro = 1.94

total_vege = price_kilo_vege * total_vege_kilo
total_fruit = price_kilo_fruit * total_fruit_kilo

total = total_vege + total_fruit

abs_total = total / euro

print(f'{abs_total:.2f}')