sea_travel = int(input())
mountain_travel = int(input())

sea = sea_travel
mountain = mountain_travel
sea_price = 0
mountain_price = 0

while True:
    command = input()
    if command == 'sea':
        if sea <= 0:
            pass
        else:
            sea -= 1
            sea_price += 680
    elif command == 'mountain':
        if mountain <= 0:
            pass
        else:
            mountain -= 1
            mountain_price += 499
    elif command == 'Stop':
        print(f'Profit: {sea_price + mountain_price} leva.')
        break

    if sea <= 0 and mountain <= 0:
        print(f'Good job! Everything is sold.')
        print(f'Profit: {sea_price + mountain_price} leva.')
        break



