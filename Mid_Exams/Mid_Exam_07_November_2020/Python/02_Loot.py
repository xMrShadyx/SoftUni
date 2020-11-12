initial_loot = input().split("|")

poped_items = []
while True:
	commands = input()
	if commands == "Yohoho!":
		break

	token = commands.split()
	command = token[0]

	if command == "Loot":
		for el in token[1:]:
			if el not in initial_loot:
				initial_loot.insert(0, el)

	elif command == "Drop":
		index = int(token[1])
		RANGE = range(len(initial_loot))
		if index in RANGE:
			poped_item = initial_loot.pop(index)
			initial_loot.append(poped_item)

	elif command == "Steal":
		count = int(token[1])
		poped_items = [item for item in initial_loot][-count:]
		for item in poped_items:
			initial_loot.remove(item)
		print(f"{', '.join(poped_items)}")

coins = 0
for item in initial_loot:
	coins += len(item)

if len(initial_loot) != 0:
	average_sum = coins / len(initial_loot)
	print(f"Average treasure gain: {average_sum:.2f} pirate credits.")
else:
	print(f"Failed treasure hunt.")