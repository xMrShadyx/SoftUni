cards = input().split()

team_a = [1] * 11
team_b = [1] * 11

for card in cards:
    tokens = card.split('-')
    team = tokens[0]
    player = int(tokens[1])

    if team == "A":
        team_a[player - 1] = 0
    else:
        team_b[player - 1] = 0

team_a_count = 0
team_b_count = 0

for i in range(11):
    team_a_count += team_a[i]
    team_b_count += team_b[i]

print(f'Team A - {team_a_count}; Team B - {team_b_count}')

if team_a_count < 7 or team_b_count < 7:
    print('Game was terminated!')
