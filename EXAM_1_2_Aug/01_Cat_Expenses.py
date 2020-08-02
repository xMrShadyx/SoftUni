bed_price = float(input())
toilet_price = float(input())
year = 12

price_bed = bed_price
price_toiled = toilet_price
price_food = (toilet_price * 0.25) + toilet_price
price_toys = price_food * 0.5
price_doc = (price_toys * 0.1) + price_toys

ext_expenses = (price_toiled + price_food + price_toys + price_doc) * 0.05
ext = price_toiled + price_food + price_toys + price_doc
total_expenses = price_bed + year * ext + year * ext_expenses

print(f'{total_expenses:.2f} lv.')


