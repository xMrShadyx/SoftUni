team_a = [f"A-{i}" for i in range(1, 12)]
team_b = [f"B-{i}" for i in range(1, 12)]

players_kicked = input().split()

for i in players_kicked:

    if i in team_a:
        team_a.remove(i)
        if len(team_a) < 7:
            break

    if i in team_b:
        team_b.remove(i)
        if len(team_b) < 7:
            break

print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
if len(team_a) < 7 or len(team_b) < 7:
    print("Game was terminated")
