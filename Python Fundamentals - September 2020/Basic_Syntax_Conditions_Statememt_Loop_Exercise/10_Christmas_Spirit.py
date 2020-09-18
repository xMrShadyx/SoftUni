quantity = int(input())
days = int(input())
spirit = 0
total = 0

ornament_set = 2
tree_skirt = 5
tree_garlands = 3
tree_lights = 15

for i in range(1, days + 1):
    if i % 11 == 0:
        quantity += 2
    if i % 2 == 0:
        total += ornament_set * quantity
        spirit += 5
    if i % 3 == 0:
        total += (tree_skirt + tree_garlands) * quantity
        spirit += 13
    if i % 5 == 0:
        total += tree_lights * quantity
        spirit += 17

    if i % 10 == 0:
        spirit -= 20
        total += tree_skirt + tree_garlands + tree_lights
        if i == days:
            spirit -= 30
    if i % 3 == 0 and i % 5 == 0:  # if i % 15 == 0:
        spirit += 30

print(f"Total cost: {total}")
print(f"Total spirit: {spirit}")