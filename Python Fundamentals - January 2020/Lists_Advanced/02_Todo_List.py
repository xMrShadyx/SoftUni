tasks = []

while True:
    command = input()
    if command == 'End':
        break
    tokens = command.split('-', maxsplit=1)
    priority = int(tokens[0])
    task = tokens[1]
    tasks.append((priority, task))

task_in_priority = [task_name for priority, task_name in sorted(tasks)]

print(task_in_priority)
