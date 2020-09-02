clients = int(input())
total_clients = clients

price = 0
total_price = 0
items = 0
total_items = 0

while total_clients > 0:
    while True:
        item = input()
        if item == 'basket':
            price += 1.50
            total_price += 1.50
            total_items += 1
        elif item == 'wreath':
            price += 3.8
            total_price += 3.8
            total_items += 1
        elif item == 'chocolate bunny':
            price += 7
            total_price += 7
            total_items += 1
        elif item == 'Finish':
            if total_items % 2 == 0:
                price1 = price * 0.20
                price = abs(price1 - price)
                total_price = abs(total_price - price1)
            print(f"You purchased {total_items} items for {price:.2f} leva.")
            price = 0
            items = 0
            total_items = 0
            break
    total_clients -= 1
print(f"Average bill per client is: {(total_price / clients):.2f} leva.")