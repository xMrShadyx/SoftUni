items = input().split(", ")


def collect_item(items_list, i):
	if i not in items_list:
		items_list.append(i)
	return items_list


def drop_item(items_list, i):
	if i in items_list:
		items_list.remove(i)
	return items_list


def combine_items(items_list, i):
	old_item = i.split(":")[0]
	new_item = i.split(":")[1]
	if old_item in items_list:
		index_old_item = items_list.index(old_item)
		index_new_item = index_old_item + 1
		items_list.insert(index_new_item, new_item)
	return items_list


def renew_item(items_list, i):
	if i in items_list:
		items_list.remove(i)
		items_list.append(i)
	return items_list


data = input()

while not data == "Craft!":
	command, item = data.split(" - ")

	if command == 'Collect':
		items = collect_item(items, item)
	elif command == 'Drop':
		items = drop_item(items, item)
	elif command == 'Combine Items':
		items = combine_items(items, item)
	elif command == 'Renew':
		renew_item(items, item)
	data = input()

print(", ".join(items))
