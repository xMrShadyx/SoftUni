stadium_capacity = int(input())
amount_of_fans = int(input())

sector_a = 0
sector_b = 0
sector_v = 0
sector_g = 0

for i in range(amount_of_fans):
    player_sector = input()
    if player_sector == 'A':
        sector_a += 1
    elif player_sector == 'B':
        sector_b += 1
    elif player_sector == 'V':
        sector_v += 1
    elif player_sector == 'G':
        sector_g += 1

let_a = (sector_a / amount_of_fans) * 100
let_b = (sector_b / amount_of_fans) * 100
let_v = (sector_v / amount_of_fans) * 100
let_g = (sector_g / amount_of_fans) * 100
let_total = (amount_of_fans / stadium_capacity) * 100

print(f'{let_a:.2f}%')
print(f'{let_b:.2f}%')
print(f'{let_v:.2f}%')
print(f'{let_g:.2f}%')
print(f'{let_total:.2f}%')
