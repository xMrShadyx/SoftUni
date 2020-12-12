def move(message, n):
	letters_to_move = message[:n]
	second_part = message[n:]
	result = second_part + letters_to_move
	return result


def insert_value(message, i, val):
	first_part = message[:i]
	second_part = message[i:]
	result = first_part + val + second_part
	return result


encrypted_message = input()
data = input()

while not data == "Decode":
	splitter_data = data.split("|")
	command = splitter_data[0]
	if command == "Move":
		n_letters = int(splitter_data[1])
		encrypted_message = move(encrypted_message, n_letters)

	elif command == "Insert":
		index = int(splitter_data[1])
		value = splitter_data[2]
		encrypted_message = insert_value(encrypted_message, index, value)

	elif command == "ChangeAll":
		sub_str = splitter_data[1]
		value = splitter_data[2]
		encrypted_message = encrypted_message.replace(sub_str, value)
	data = input()


print(f"The decrypted message is: {encrypted_message}")
