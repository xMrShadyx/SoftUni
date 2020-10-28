neighborhood = [int(el) for el in input().split("@")]

command = input()
position = 0

while not command == "Love!":
	length = int(command.split()[1])
	position += length
	if position < len(neighborhood):
		if neighborhood[position] == 0:
			print(f"Place {position} already had Valentine's day.")
		else:
			neighborhood[position] -= 2
			if neighborhood[position] == 0:
				print(f"Place {position} has Valentine's day.")
	else:
		position = 0
		if neighborhood[position] == 0:
			print(f"Place {position} already had Valentine's day.")
		else:
			neighborhood[position] -= 2
			if neighborhood[position] == 0:
				print(f"Place {position} has Valentine's day.")

	command = input()

print(f"Cupid's last position was {position}.")
if sum(neighborhood) == 0:
	print("Mission was successful.")
else:
	count = [el for el in neighborhood if el != 0]
	print(f"Cupid has failed {len(count)} places.")