index_of_element = input().split()
number_of_moves = 0

command = input()


while not command == 'end':
	firstInx, secondInx = command.split()

	number_of_moves += 1
	if int(firstInx) < 0 or int(firstInx) > len(index_of_element) - 1 or int(secondInx) < 0 or int(secondInx) > len(index_of_element) - 1 or firstInx == secondInx:
		print("Invalid input! Adding additional elements to the board")
		half_list = len(index_of_element) // 2
		index_of_element.insert(half_list, f"-{number_of_moves}a")
		index_of_element.insert(half_list, f"-{number_of_moves}a")
	else:
		num1 = index_of_element[int(firstInx)]
		num2 = index_of_element[int(secondInx)]

		if num1 == num2:
			index_of_element.remove(num1)
			index_of_element.remove(num2)
			print(f"Congrats! You have found matching elements - {num1}!")
		else:
			print("Try again!")

	if len(index_of_element) == 0:
		print(f"You have won in {number_of_moves} turns!")
		break

	command = input()

if len(index_of_element) != 0:
	print("Sorry you lose :(")
	print(" ".join([el for el in index_of_element]))
