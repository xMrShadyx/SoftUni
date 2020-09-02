price_wheat = float(input())
amount_wheat = float(input())
amount_sugar = float(input())
amount_eggs = int(input())
amount_maya = int(input())

price_sugar = price_wheat * 0.75
price_eggs = price_wheat * 1.1
price_maya = price_sugar * 0.2

price_for_wheat = price_wheat * amount_wheat
price_for_sugar = amount_sugar * price_sugar
price_for_eggs = price_eggs * amount_eggs
price_for_maya = price_maya * amount_maya

total = price_for_wheat + price_for_sugar + price_for_eggs + price_for_maya

print(f"{total:.2f}")