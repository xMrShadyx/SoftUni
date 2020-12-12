# data = input().split()
#
# products = {}
#
# for index in range(0, len(data), 2):
# 	key = data[index]
# 	value = int(data[index + 1])
# 	products[key] = value
#
# products_to_search = input().split()
#
# for product in products_to_search:
# 	if product in products:
# 		print(f"We have {products[product]} of {product} left")
# 	else:
# 		print(f"Sorry, we don't have {product}")

def handle_product(product, products_quantity_dict):
	if product in products_quantity_dict:
		print(f"We have {products_quantity_dict[product]} of {product} left")
	else:
		print(f"Sorry, we don't have {product}")


def extract_products_quantities(products_quantity_str):
	values = products_quantity_str.split(' ')
	n = len(values)
	return {values[i]: int(values[i + 1]) for i in range(0, n, 2)}


def solve(products_quantity_str, products_str):
	products_quantity_dict = extract_products_quantities(products_quantity_str)
	[handle_product(product, products_quantity_dict) for product in products_str.split(' ')]





solve(input(), input())
# solve('cheese 10 bread 5 ham 10 chocolate 3', 'jam cheese ham tomatoes')