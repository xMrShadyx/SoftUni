import sys

player = input()

points_max = -sys.maxsize

while player != 'Stop':
    points = 0
    for index, letter in enumerate(player):
        num = int(input())
        if num == ord(letter):
            points += 10
        else:
            points += 2
    if points >= points_max:
        points_max = points
        player_max = player
    player = input()

print(f"The winner is {player_max} with {points_max} points!")
