type_gas = input()
amount_gas = float(input())
club_card = input()

gasoline = 2.22
diesel = 2.33
gas = 0.93

total = 0

if club_card == "Yes":
    gas += - 0.08
    gasoline += - 0.18
    diesel += - 0.12

if type_gas == 'Gas':
    total = amount_gas * gas
elif type_gas == 'Gasoline':
    total = amount_gas * gasoline
elif type_gas == 'Diesel':
    total = amount_gas * diesel

    
if 20 <= amount_gas <= 25:
    total = total * 0.92
elif amount_gas > 25:
    total = total * 0.90

print(f"{total:.2f} lv.")


    