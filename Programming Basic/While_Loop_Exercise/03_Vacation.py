needed_money = float(input())
saved_money = float(input())

days_money_spent = 0
total_days = 0

while True:
    action = input()
    money = float(input())
    total_days += 1

    if action == 'save':
        saved_money += money
        days_money_spent = 0
    else:
        saved_money -= money
        days_money_spent += 1
        if saved_money < 0:
            saved_money = 0

    if days_money_spent == 5:
        print('You can\'t save the money.')
        print(total_days)
        break

    if saved_money >= needed_money:
        print(f"You saved the money for {total_days} days.")
        break
