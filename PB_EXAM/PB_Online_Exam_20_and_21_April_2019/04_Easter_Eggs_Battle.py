player_one = int(input())
player_two = int(input())

cmd = input()

while cmd != "End of battle":
    turn = str(cmd)
    if turn == 'one':
        player_two -= 1
    elif turn == 'two':
        player_one -= 1

    if player_one == 0 or player_two == 0:
        break

    cmd = input()

if cmd == 'End of battle':
    print(f'Player one has {player_one} eggs left.')
    print(f'Player two has {player_two} eggs left.')
elif player_one < player_two:
    print(f'Player one is out of eggs. Player two has {player_two} eggs left.')
else:
    print(f'Player two is out of eggs. Player one has {player_one} eggs left.')