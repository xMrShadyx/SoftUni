amount_cozunaks = int(input())
total_cozunaks = amount_cozunaks

best_chef = ''
chef_name = ''
total_score = 0
best_score = 0

while total_cozunaks > 0:
    name = input()
    chef_name = name
    while True:
        points = input()
        if points == 'Stop':
            break
        else:
            total_score += int(points)

    if best_score < total_score:
        best_score = total_score
        best_chef = chef_name
        print(f"{best_chef} has {best_score} points.")
        print(f"{best_chef} is the new number 1!")
        total_score = 0
    else:
        print(f"{chef_name} has {total_score} points.")
        total_score = 0

    total_cozunaks -= 1

print(f"{best_chef} won competition with {best_score} points!")