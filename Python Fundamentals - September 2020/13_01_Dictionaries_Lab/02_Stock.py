# my_dict = {'name': 'Peter', 'age': 22}
# if 'name' in my_dict:
# 	print(my_dict['name'])
#
# if 'name' in my_dict.keys():
# 	print(my_dict['name'])

# cheese 10 bread 5 ham 10 chocolate 3
# jam cheese ham tomatoes


def get_stock(raw_data):
	data = raw_data.split(" ")
	result = {}
	for i in range(0, len(data), 2):
		key = data[i]
		value = data[i + 1]
		result[key] = int(value)
	return result


def check_availability(stocks: dict, search_products: list[str]):
	result = ''
	for product in search_products:
		if not stock.get(product):
			result += f"Sorry, we don't have {product}\n"
		else:
			result += f"We have {stocks[product]} of {product} left\n"
	return result


stock = get_stock(input())
print(check_availability(stock, input().split(' ')))