note = input()

todo_list = [0 for _ in range(10)]

while not note == 'End':
	data = note.split("-")
	importance = int(data[0])
	task = data[1]
	todo_list.insert(importance, task)
	note = input()

result = [task for task in todo_list if not task == 0]

print(result)