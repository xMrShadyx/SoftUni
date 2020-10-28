shopping_list = input().split("!")


command = input()


def check_item_exist(item_list, item_search):
	return True if item_search in item_list else False


while not command == "Go Shopping!":
	try:
		command_type, item = command.split()
	except ValueError:
		command_type, item, value = command.split()

	if command_type == "Urgent":
		if not check_item_exist(shopping_list, item):
			shopping_list.insert(0, item)

	elif command_type == "Unnecessary":
		if check_item_exist(shopping_list, item):
			shopping_list.remove(item)

	elif command_type == 'Correct':
		if check_item_exist(shopping_list, item):
			current_index = shopping_list.index(item)
			shopping_list[current_index] = value

	elif command_type == 'Rearrange':
		if check_item_exist(shopping_list, item):
			shopping_list.remove(item)
			shopping_list.append(item)

	command = input()

print(", ".join(shopping_list))