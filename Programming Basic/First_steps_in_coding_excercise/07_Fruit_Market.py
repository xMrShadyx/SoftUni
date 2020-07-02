# ⦁	Цена на ягодите в лева – реално число;
price_strawberry = float(input())
# ⦁	Количество на бананите в килограми – реално число;
amount_kg_bananas = float(input())
# ⦁	Количество на портокалите в килограми – реално число;
amount_kg_oranges = float(input())
# ⦁	Количество на малините в килограми – реално число;
amount_kg_blackberry = float(input())
# ⦁	Количество на ягодите в килограми – реално число.
amount_kg_strawberry = float(input())

blackberry_price = price_strawberry / 2
orange_price = blackberry_price - (blackberry_price * 0.4)
bananas_price = blackberry_price - (blackberry_price * 0.8)

price_for_blackberry = blackberry_price * amount_kg_blackberry
price_for_oranges = amount_kg_oranges * orange_price
price_for_bananas = bananas_price * amount_kg_bananas
price_for_strawberry = price_strawberry * amount_kg_strawberry

total = price_for_bananas + price_for_oranges + price_for_blackberry + price_for_strawberry

print(total)