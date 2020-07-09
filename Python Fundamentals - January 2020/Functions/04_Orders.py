def find_price(product):
    if product == 'coffee':
        return 1.5
    if product == 'water':
        return 1.0
    if product == 'coke':
        return 1.4
    if product == 'snacks':
        return 2.0


def get_order(product, quantity):
    price_per_unit = find_price(product)
    if price_per_unit is None:
        return 0.0
    return price_per_unit * quantity


product = input()
quantity = int(input())

print(f'{get_order(product, quantity):.2f}')
