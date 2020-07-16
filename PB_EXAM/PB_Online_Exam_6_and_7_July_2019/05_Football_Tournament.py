team_name = input()
played_games = int(input())

points = 0
w = 0
d = 0
l = 0

for i in range(played_games):
    games = str(input())

    if games == 'W':
        w += 1
        points += 3
    elif games == 'D':
        d += 1
        points += 1
    elif games == 'L':
        l += 1


if played_games == 0:
    print(f"{team_name} hasn't played any games during this season.")
else:
    total_points = points
    win_rate = (w / played_games) * 100
    print(f"{team_name} has won {total_points} points during this season.")
    print("Total stats:")
    print(f"## W: {w}")
    print(f"## D: {d}")
    print(f"## L: {l}")
    print(f"Win rate: {win_rate:.2f}%")

