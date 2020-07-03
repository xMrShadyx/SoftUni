budged = float(input())
category = input()
amount_of_peoples = int(input())

transport = 0

if amount_of_peoples >= 1 and amount_of_peoples <= 4:
    transport = budged * 0.75
elif amount_of_peoples >= 5 and amount_of_peoples <= 9:
    transport = budged * 0.60
elif amount_of_peoples >= 10 and amount_of_peoples <= 24:
    transport = budged * 0.50
elif amount_of_peoples >= 25 and amount_of_peoples <= 49:
    transport = budged * 0.40
elif amount_of_peoples > 50:
    transport = budged * 0.25
    
if category == "VIP":
    left_over = budged - transport
    ticket = amount_of_peoples * 499.99
    total = left_over - ticket
    if left_over < ticket:
        print(f"Not enough money! You need {abs(total):.2f} leva.")
    else:
        print(f"Yes! You have {abs(total):.2f} leva left.")

elif category == "Normal":
    left_over = budged - transport
    ticket = amount_of_peoples * 249.99
    total = left_over - ticket
    if left_over < ticket:
        print(f"Not enough money! You need {abs(total):.2f} leva.")
    else:
        print(f"Yes! You have {abs(total):.2f} leva left.")

