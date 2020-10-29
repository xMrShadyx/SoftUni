command = input()
total_price = 0
tax = 0

while not command == "special" or not command == "regular":
	if command == "special":
		if total_price == 0:
			print("Invalid order!")
			break
		else:
			vip = (total_price + tax) * 0.1
			last = (total_price + tax) - vip
			print("Congratulations you've just bought a new computer!")
			print(f"Price without taxes: {total_price:.2f}$")
			print(f"Taxes: {tax:.2f}$")
			print("-----------")
			print(f"Total price: {last:.2f}$")
			break
	elif command == 'regular':
		if total_price == 0:
			print("Invalid order!")
			break
		else:
			print("Congratulations you've just bought a new computer!")
			print(f"Price without taxes: {total_price:.2f}$")
			print(f"Taxes: {tax:.2f}$")
			print("-----------")
			print(f"Total price: {total_price + tax:.2f}$")
			break
	else:
		if float(command) < 0:
			print("Invalid price!")
		else:
			total_price += float(command)
			tax += float(command) * 0.2

	command = input()