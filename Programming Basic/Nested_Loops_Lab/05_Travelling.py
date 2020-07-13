while True:
    destination = input()
    if destination == 'End':
        break
    min_budget = float(input())

    current_money = 0
    while current_money < min_budget:
        money = float(input())
        current_money += money
    print(f"Going to {destination}!")
