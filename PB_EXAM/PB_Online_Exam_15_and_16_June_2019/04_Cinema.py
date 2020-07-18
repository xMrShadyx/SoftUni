command = input()

available_seats = 0
price = 0

while command != 'Movie time!':
    taken_seats = 0
    available_seats = int(command)

    while taken_seats <= available_seats:
        taken_seats += int(input())
        price = taken_seats * 5

    if taken_seats % 3 != 0:
        price = price - 5

    if taken_seats <= available_seats:
        diff = available_seats - taken_seats
        print(f'"There are {diff} seats left in the cinema.')
        print(f"Cinema income - {price} lv.")

    elif taken_seats > available_seats:
        print("The cinema is full.")
        print(f"Cinema income - {price} lv.")

    command = input()

