needed_exp = float(input())
count_battles = int(input())
count = 0
total_exp = 0
while count_battles > 0:
	exp_per_battle = int(input())
	count += 1
	if count % 3 == 0:
		exp_per_battle += exp_per_battle * 0.15
	if count % 5 == 0:
		exp_per_battle -= exp_per_battle - (exp_per_battle * 0.90)
	if count % 15 == 0:
		exp_per_battle += exp_per_battle * 0.05
	total_exp += exp_per_battle

	if total_exp >= needed_exp:
		break

	count_battles -= 1

if total_exp >= needed_exp:
	print(f"Player successfully collected his needed experience for {count} battles.")
else:
	print(f"Player was not able to collect the needed experience, {needed_exp - total_exp:.2f} more needed.")
