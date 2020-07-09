import math
amount_days = int(input())
amount_left_food = int(input())
dog_food_per_day = float(input())
cat_food_per_day = float(input())
turtle_food_per_day = float(input())

dog = amount_days * dog_food_per_day
cat = amount_days * cat_food_per_day
turtle = amount_days * turtle_food_per_day / 1000

total_needed_food = dog + cat + turtle

if total_needed_food <= amount_left_food:
    diff = math.floor(amount_left_food - total_needed_food)
    print(f"{diff} kilos of food left.")
else:
    diff = math.ceil(total_needed_food - amount_left_food)
    print(f"{diff} more kilos of food are needed.")
    