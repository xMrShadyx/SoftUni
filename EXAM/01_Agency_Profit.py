avio_company_name = input()
amount_old_tickets = int(input())
amount_kid_tickets = int(input())
price_old_tickets = float(input())
service_tax = float(input())

kid_price = price_old_tickets * 0.3
price_old_tax = price_old_tickets + service_tax
kid_price_tax = kid_price + service_tax
total = (amount_kid_tickets * kid_price_tax) + (amount_old_tickets * price_old_tax)
profit = total * 0.2

print(f"The profit of your agency from {avio_company_name} tickets is {profit:.2f} lv.")
