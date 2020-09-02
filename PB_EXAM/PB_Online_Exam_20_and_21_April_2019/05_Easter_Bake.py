from math import ceil

amount_cozunaks = int(input())

sugar_am = 0
flour_am = 0
used_flour = 0
used_sugar = 0
max_flour = 0
max_sugar = 0

for i in range(1, amount_cozunaks + 1):
    sugar = int(input())
    sugar_am += sugar

    if sugar > max_sugar:
        max_sugar = sugar

    flour = int(input())
    flour_am += flour

    if flour > max_flour:
        max_flour = flour

used_sugar = sugar_am / 950
used_flour = flour_am / 750
print(f"Sugar: {ceil(used_sugar)}")
print(f"Flour: {ceil(used_flour)}")
print(f"Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.")
