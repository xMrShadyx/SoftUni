from math import ceil

amount_of_guests = int(input())
budget = float(input())

amount_of_cozunaks = ceil(amount_of_guests / 3)
amount_of_eggs = amount_of_guests * 2

price_for_cozunaks = amount_of_cozunaks * 4
price_for_eggs = amount_of_eggs * 0.45

total = price_for_eggs + price_for_cozunaks
diff = abs(total - budget)

if total > budget:
    print(f"Lyubo doesn't have enough money.")
    print(f"He needs {diff:.2f} lv. more.")
else:
    print(f"Lyubo bought {amount_of_cozunaks} Easter bread and {amount_of_eggs} eggs.")
    print(f"He has {diff:.2f} lv. left.")
