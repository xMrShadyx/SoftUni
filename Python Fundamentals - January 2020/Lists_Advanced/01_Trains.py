n = int(input())

wagons = [0] * n

while True:
    command = input()
    if command == 'End':
        break

    tokens = command.split(' ')
    command = tokens[0]
    if command == 'add':
        people_to_add = int(tokens[1])
        wagons[-1] += people_to_add
    elif command == 'insert':
        index = int(tokens[1])
        people_to_insert = int(tokens[2])
        wagons[index] += people_to_insert
    elif command == 'leave':
        index = int(tokens[1])
        people_to_insert = int(tokens[2])
        wagons[index] -= people_to_insert

print(wagons)
