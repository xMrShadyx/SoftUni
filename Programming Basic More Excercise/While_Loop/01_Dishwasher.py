preparat = int(input())
total_detergents = preparat * 750

command = input()
total1 = 0

saved_tendjeri = 0
saved_chinii = 0

count = 0
while command != 'End':
    count += 1
    chinii = 0
    tendjeri = 0
    total_tendjeri = 0
    total_chinii = 0

    washed_items = int(command)
    if count % 3 == 0:
        saved_tendjeri += washed_items
        total_tendjeri += washed_items
        tendjeri += 15
        total_detergents -= total_tendjeri * tendjeri
    else:
        chinii += 5
        saved_chinii += washed_items
        total_chinii += washed_items
        total_detergents -= total_chinii * chinii

    if total_detergents < 0:
        break
    else:
        command = input()

if total_detergents >= preparat:
    diff = total_detergents - preparat
    print(f"Detergent was enough!")
    print(f"{saved_chinii} dishes and {saved_tendjeri} pots were washed.")
    print(f"Leftover detergent {total_detergents} ml.")
else:
    print(f"Not enough detergent, {abs(total_detergents)} ml. more necessary!")


