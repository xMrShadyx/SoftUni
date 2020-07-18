actor_name = input()
actor_points = float(input())
jury = int(input())

points = actor_points

for i in range(jury):
    jury_name = input()
    jury_points = float(input())
    jury_name_len = len(jury_name)
    points += ((jury_name_len * jury_points) / 2)
    if points > 1250.5:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {points:.1f}!")
        break


if points < 1250.5:
    diff = 1250.5 - points
    print(f"Sorry, {actor_name} you need {diff:.1f} more!")


    

