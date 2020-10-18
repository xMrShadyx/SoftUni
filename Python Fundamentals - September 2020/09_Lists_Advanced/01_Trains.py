number_of_wagons = int(input())

train = [0 for _ in range(number_of_wagons)]


command = input()

while not command == "End":
	data = command.split()
	if data[0] == "add":
		number_of_people = int(data[1])
		train[-1] += number_of_people

	if data[0] == 'insert':
		index = int(data[1])
		number_of_people = int(data[2])
		train[index] += number_of_people

	if data[0] == 'leave':
		index = int(data[1])
		number_of_people = int(data[2])
		train[index] -= number_of_people
	command = input()

print(train)