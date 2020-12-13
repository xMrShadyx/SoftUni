import re

n = int(input())

message_pattern = r"([*]|[@])([A-Z][a-z]{2,})(\1)(:\s)((\[[A-Za-z]\]\|){3})$"
chars_pattern = "\w"

for _ in range(n):
	line = input()
	list_of_chars = []

	valid_message = re.findall(message_pattern, line)

	if valid_message:
		for message in valid_message:
			chars = re.findall(chars_pattern, message[4])
			for char in chars:
				list_of_chars.append(ord(char))

			list_of_chars_str = list(map(str, list_of_chars))
			print(f"{message[1]}: {' '.join(list_of_chars_str)}")

	else:
		print("Valid message not found!")