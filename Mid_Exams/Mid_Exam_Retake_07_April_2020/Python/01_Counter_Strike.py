# Author: Lion963

energy = int(input())
wins = 0

distance = input()

while not distance == 'End of battle':
    distance = int(distance)

    if energy >= distance:
        wins += 1
        energy -= distance
        if wins % 3 == 0:
            energy += wins
    else:
        print(f'Not enough energy! Game ends with {wins} won battles and {energy} energy')
        break

    distance = input()

if distance == 'End of battle':
    print(f'Won battles: {wins}. Energy left: {energy}')