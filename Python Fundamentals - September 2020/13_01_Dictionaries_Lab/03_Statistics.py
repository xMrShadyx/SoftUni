<<<<<<< HEAD
from collections import defaultdict


# stocks = {}
stocks = defaultdict(int)
while True:
	command = input()
	if command == 'statistics':
		break

	product, quantity = command.split(': ')
	stocks[product] += int(quantity)
	# if product in stocks:
	# 	stocks[product] += int(quantity)
	# else:
	# 	stocks[product] = int(quantity)

print("Products in stock:")
for product, quantity in stocks.items():
	print(f" - {product}: {quantity}")

print(f"Total products {len(stocks.keys())}")
print(f"Total quantity {sum(stocks.values())}")
=======
from collections import defaultdict


# stocks = {}
stocks = defaultdict(int)
while True:
	command = input()
	if command == 'statistics':
		break

	product, quantity = command.split(': ')
	stocks[product] += int(quantity)
	# if product in stocks:
	# 	stocks[product] += int(quantity)
	# else:
	# 	stocks[product] = int(quantity)

print("Products in stock:")
for product, quantity in stocks.items():
	print(f" - {product}: {quantity}")

print(f"Total products {len(stocks.keys())}")
print(f"Total quantity {sum(stocks.values())}")
>>>>>>> 06f2e621b68de7dbe64b4c1441e71917f616ece7
