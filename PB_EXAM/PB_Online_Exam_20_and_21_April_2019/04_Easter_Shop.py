amount_starting_eggs = int(input())

sold_eggs = 0

cmd = input()

while cmd != "Close":
    operation = str(cmd)
    amount = int(input())

    if operation == 'Buy' and amount > amount_starting_eggs:
        print(f"Not enough eggs in store!")
        print(f"You can buy only {amount_starting_eggs}.")
        break

    if operation == "Buy":
        amount_starting_eggs -= amount
        sold_eggs += amount
    elif operation == "Fill":
        amount_starting_eggs += amount

    if amount_starting_eggs < 0:
        print(f"Not enough eggs in store!")
        print(f"You can buy only {amount_starting_eggs}.")

    cmd = input()

if cmd == 'Close':
    print("Store is closed!")
    print(f"{sold_eggs} eggs sold.")
