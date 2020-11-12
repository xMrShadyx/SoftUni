price_ratings_input = input().split()
entry_point = int(input())
item_type = input()
type_price_rating = input()

price_ratings = list(map(int, price_ratings_input))

left = [left for left in price_ratings[:entry_point]]
right = [right for right in price_ratings[entry_point + 1:]]

entry_point_value = price_ratings[entry_point]

if item_type == "cheap":
	left = list(filter(lambda x: x < entry_point_value, left))
	right = list(filter(lambda x: x < entry_point_value, right))
elif item_type == "expensive":
	left = list(filter(lambda x: x >= entry_point_value, left))
	right = list(filter(lambda x: x >= entry_point_value, right))

if type_price_rating == "positive":
	left = [number for number in left if number > 0]
	right = [number for number in right if number > 0]
elif type_price_rating == "negative":
	left = [number for number in left if number < 0]
	right = [number for number in right if number < 0]

if sum(left) >= sum(right):
	print(f"Left - {sum(left)}")
else:
	print(f"Right - {sum(right)}")