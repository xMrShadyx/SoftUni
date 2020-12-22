<<<<<<< HEAD
product_prices = {}
products_quantities = {}

data = input()

while not data == 'buy':
	product, price, quantity = data.split()
	price = float(price)
	quantity = int(quantity)

	if product not in product_prices:
		product_prices[product] = price
		products_quantities[product] = quantity
	else:
		product_prices[product] = price
		products_quantities[product] += quantity

	data = input()

for product, price in product_prices.items():
	total_price = price * products_quantities[product]
	print(f"{product} -> {total_price:.2f}")
=======
product_prices = {}
products_quantities = {}

data = input()

while not data == 'buy':
	product, price, quantity = data.split()
	price = float(price)
	quantity = int(quantity)

	if product not in product_prices:
		product_prices[product] = price
		products_quantities[product] = quantity
	else:
		product_prices[product] = price
		products_quantities[product] += quantity

	data = input()

for product, price in product_prices.items():
	total_price = price * products_quantities[product]
	print(f"{product} -> {total_price:.2f}")
>>>>>>> 06f2e621b68de7dbe64b4c1441e71917f616ece7
