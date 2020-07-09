import math

junior_racers = int(input())
senior_racers = int(input())
type_race = input()

tax = 0
expenses = 0

if type_race == "trail":
    juniors = junior_racers * 5.5
    seniors = senior_racers * 7
    total_amount = juniors + seniors
    expenses = total_amount * 0.95

elif type_race == "cross-country":
    total_racers = junior_racers + senior_racers
    juniors = junior_racers * 8
    seniors = senior_racers * 9.5
    total_amount = juniors + seniors
    if total_racers >= 50:
        tax = total_amount * 0.75
        expenses = tax * 0.95
    else:
        expenses = total_amount * 0.95

elif type_race == "downhill":
    juniors = junior_racers * 12.25
    seniors = senior_racers * 13.75
    total_amount = juniors + seniors
    expenses = total_amount * 0.95

elif type_race == "road":
    juniors = junior_racers * 20
    seniors = senior_racers * 21.50
    total_amount = juniors + seniors
    expenses = total_amount * 0.95

print(f"{expenses:.2f}")
