data = input().split()

products = {}

for index in range(0, len(data), 2):
    key = data[index]
    value = int(data[index + 1])
    products[key] = value

print(products)


# V. 2
def solve(bakery_str):
    values = bakery_str.split(' ')
    bakery = {}
    n = len(values)
    for i in range(0, n, 0):
        food = values[i]
        quantity = int(values[i + 1])
        bakery[food] = quantity
    print(bakery)


solve(input())


# V. 3
def solve(bakery_str):
    values = bakery_str.split(' ')
    n = len(values)
    bakery = {values[i]: int(value[i+1]) for i in range(0, n, 2)}
    print(bakery)


solve(input())