'''
Add:Mark:1000:5
Add:Clark:1000:3
Attack:Clark:Mark:500
Add:Allison:2500:5
Attack:Clark:Mark:300
Add:Charlie:4000:10
Attack:Clark:Mark:500
result

Add:Bonie:3000:5
Add:Kent:10000:10
Add:Johnny:4000:10
Attack:Johnny:Bonnie:400
Add:Chicken:1000:1
Add:Rabbit:3000:5
Add:Buggy:1259:10
Delete:Kent
Attack:Chicken:Rabbit:1000
Result
'''

from collections import defaultdict


def attack(names_dict, attacker_name, defender_name, damage):
	if attacker_name in names_dict and defender_name in names_dict:

		if not names_dict[defender_name]["health"] - damage > 0:
			del names_dict[defender_name]
			print(f"{defender_name} was disqualified!")
		else:
			names_dict[defender_name]["health"] -= damage

		if not names_dict[attacker_name]["energy"] - MAGIC_NUMBER > 0:
			del names_dict[attacker_name]
			print(f"{attacker_name} was disqualified!")
		else:
			names_dict[attacker_name]["energy"] -= MAGIC_NUMBER

	return names_dict


def delete(names_dict, username):
	if username == "All":
		names_dict.clear()

	if username in names_dict:
		del names_dict[username]

	return names_dict


def add(names_dict, name, health, energy):
	if name in names_dict:
		names_dict[name]["health"] += health
		return names_dict

	names_dict[name]["health"] = health
	names_dict[name]["energy"] = energy

	return names_dict


names_dict = defaultdict(dict)
MAGIC_NUMBER = 1

while True:
	commands = input()

	if commands == "Results":
		break

	token = commands.split(":")
	command = token[0]

	if command == "Add":
		name = token[1]
		health = int(token[2])
		energy = int(token[3])

		names_dict = add(names_dict, name, health, energy)

	elif command == "Attack":
		attacker_name = token[1]
		defender_name = token[2]
		damage = int(token[3])

		names_dict = attack(names_dict, attacker_name, defender_name, damage)

	elif command == "Delete":
		username = token[1]

		names_dict = delete(names_dict, username)

if names_dict:
	print(f"People count: {len(names_dict)}")

	sorted_names = sorted(names_dict.items(), key=lambda x: (-x[1]["health"], x[0]))
	for name, _ in sorted_names:
		print(f"{name} - {names_dict[name]['health']} - {names_dict[name]['energy']}")