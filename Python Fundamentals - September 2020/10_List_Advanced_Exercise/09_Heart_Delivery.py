def jumping_in_neighborhood(neighborhood):
	crnt_house = 0
	jump_cmd = input().split()
	while not jump_cmd[0] == "Love!":
		length_jump = int(jump_cmd[1])
		if crnt_house + int(length_jump) > len(neighborhood) - 1:
			crnt_house = 0
		else:
			crnt_house += length_jump
		if not neighborhood[crnt_house] == 0:
			neighborhood[crnt_house] -= 2
			if neighborhood[crnt_house] == 0:
				print(f"Place {crnt_house} has Valentine's day.")
		else:
			print(f"Place {crnt_house} already had Valentine's day.")

		jump_cmd = input().split()

	return [[i for i in neighborhood if not i == 0], crnt_house]


neighborhood = input().split("@")
neighborhood = list(map(int, neighborhood))

failed, house_stopped = jumping_in_neighborhood(neighborhood)
print(f"Cupid's last position was {house_stopped}.")
if not failed:
	print("Mission was successful.")
else:
	print(f"Cupid has failed {len(failed)} places.")
