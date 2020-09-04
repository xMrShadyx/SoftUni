voucher_price = int(input())

cmd = input()
price = 0
amount_tickets = 0
amount_other = 0

while cmd != "End":
    purchase = cmd
    if len(cmd) > 8:
        price_per_symbol = cmd[0:2]
        for i in price_per_symbol:
            price += ord(i)
        if price > voucher_price:
            break
        else:
            amount_tickets += 1
    elif len(cmd) <= 8:
        price_per_symbol = cmd[0]
        for i in price_per_symbol:
            price += ord(i)
        if price > voucher_price:
            break
        else:
            amount_other += 1

    cmd = input()

print(amount_tickets)
print(amount_other)
