type_gas = input()
amount_gas = float(input())

if type_gas == 'Gasoline':
    if amount_gas >= 25:
        print(f"You have enough gasoline.")
    else:
        print(f"Fill your tank with gasoline!")
elif type_gas == 'Diesel':
    if amount_gas >= 25:
        print(f"You have enough diesel.")
    else:
        print(f"Fill your tank with diesel!")
elif type_gas == 'Gas':
    if amount_gas >= 25:
        print(f"You have enough gas.")
    else:
        print(f"Fill your tank with gas!.")
else:
    print("Invalid fuel!")