user_name = input()
command = input()

points_max = 0

while command != 'Stop':
    points = 0
    name = user_name

    for x in name:
        list_ord = str(ord(x))
        if command in list_ord:
            points += 10
        else:
            points += 2

        if points >= points_max:
            points_max = points
            player_max = user_name
        player = input()

print(points_max)
