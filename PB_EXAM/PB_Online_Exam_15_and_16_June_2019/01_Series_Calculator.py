name = input()
amount_seasons = int(input())
time_episodes = int(input())
full_time = int(input())

adv_time = (full_time * 0.2) + full_time
spc_time = amount_seasons * 10

no_life_time = adv_time * time_episodes * amount_seasons + spc_time

print(f"Total time needed to watch the {name} series is {int(no_life_time)} minutes.")
