game_rounds = int(input())

total_points = 0
f_0_9 = 0
f_10_19 = 0
f_20_29 = 0
f_30_39 = 0
f_40_50 = 0
inv_number = 0
total_games = 0

for i in range(game_rounds):
    points_range = int(input())
    total_games += 1

    if points_range < 0 or points_range > 50:
        total_points /= 2
        inv_number += 1

    if 0 <= points_range <= 9:
        f_0_9 += 1
        total_points += points_range * 0.2
    elif 10 <= points_range <= 19:
        f_10_19 += 1
        total_points += points_range * 0.3
    elif 20 <= points_range <= 29:
        f_20_29 += 1
        total_points += points_range * 0.4
    elif 30 <= points_range <= 39:
        f_30_39 += 1
        total_points += 50
    elif 40 <= points_range <= 50:
        f_40_50 += 1
        total_points += 100


avg_f_0_9 = f_0_9 / total_games * 100
avg_f_10_19 = f_10_19 / total_games * 100
avg_f_20_29 = f_20_29 / total_games * 100
avg_f_30_39 = f_30_39 / total_games * 100
avg_f_40_50 = f_40_50 / total_games * 100
avg_inv_num = inv_number / total_games * 100

print(f'{total_points:.2f}')
print(f'From 0 to 9: {avg_f_0_9:.2f}%')
print(f'From 10 to 19: {avg_f_10_19:.2f}%')
print(f'From 20 to 29: {avg_f_20_29:.2f}%')
print(f'From 30 to 39: {avg_f_30_39:.2f}%')
print(f'From 40 to 50: {avg_f_40_50:.2f}%')
print(f'Invalid numbers: {avg_inv_num:.2f}%')