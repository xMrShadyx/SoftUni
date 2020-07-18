capacity = int(input())
command = input()

available_seats = capacity
income = 0
is_full_capacity = False

while command != 'Movie time!':
    incoming = int(command)
    bill = incoming * 5
    if incoming % 3 == 0:
        bill -= 5
    if incoming > available_seats:
        is_full_capacity = True
        break
    available_seats -= incoming
    income += bill
    command = input()

if is_full_capacity:
    print("The cinema is full.")
else:
    print(f"There are {available_seats} seats left in the cinema.")

print(f"Cinema income - {income} lv.")