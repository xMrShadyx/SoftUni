text = input()
# Mike123@somemail.com
result = text

command = input()

while not command == "Complete":
	data = command.split()

	if data[0] == "Make":
		if data[1] == "Upper":
			result = result.upper()
			print(result)
		elif data[1] == "Lower":
			result = result.lower()
			print(result)

	elif data[0] == 'GetDomain':
		domain = int(data[1])
		n = result[-domain:]
		print(n)

	elif data[0] == 'Replace':
		result = result.replace(data[1], '-')
		print(result)

	elif data[0] == 'GetUsername':
		if "@" in result:
			for x in range(len(result)):
				if result[x] == '@':
					print(result[:x])
		else:
			print(f"The email {result} doesn't contain the @ symbol.")

	elif data[0] == 'Encrypt':
		for item in result:
			print(ord(item), end=" ")

	command = input()
