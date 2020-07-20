command = input()

best_player = ''
best_score = 0

while command != "END":
    player_name = command
    player_score = int(input())

    if player_score > best_score:
        best_score = player_score
        best_player = player_name

    if best_score >= 10:
        break

    command = input()

if best_score >= 3:
    print(f"{best_player} is the best player!")
    print(f"He has scored {best_score} goals and made a hat-trick !!!")
else:
    print(f"{best_player} is the best player!")
    print(f"He has scored {best_score} goals.")
