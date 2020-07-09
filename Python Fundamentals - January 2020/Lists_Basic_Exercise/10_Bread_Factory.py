events = input().split("|")

energy = 100
coins = 100
is_closed = False

for even in events:
    args = even.split('-')
    name = args[0]
    number = int(args[1])

    if name == 'rest':
        temp = 0
        if energy + number <= 100:
            energy += number
            temp = number
        else:
            temp = 100 - energy
            energy = 100
        print(f'You gained {temp} energy')
        print(f'Current energy: {energy}')
    elif name == 'order':
        if energy - 30 >= 0:
            coins += number
            energy -= 30
            print(f"You earned {number} coins")
        else:
            energy += 50
            print('You had to rest!')
    else:
        if coins - number > 0:
            coins -= number
            print(f"You bought {name}.")
        else:
            print(f'Closed! Cannot afford {name}')
            is_closed = True
            break

if not is_closed:
    print('Day completed!')
    print(f'Coins: {coins}')
    print(f'Energy: {energy}')