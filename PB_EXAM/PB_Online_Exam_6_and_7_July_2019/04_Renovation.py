wall_height = int(input())
wall_width = int(input())
not_painted_space = int(input())

space = (wall_height * wall_width) * 4
total_litres = 0
command = input()


while command != 'Tired!':
    liters = int(command)
    total_litres += liters
    not_painted = (100 - not_painted_space) / 100
    space_p = space * not_painted

    if space_p < total_litres:
        diff = total_litres - space_p
        print(f"All walls are painted and you have {round(diff)} l paint left!")
        break
    if space_p == total_litres:
        print(f"All walls are painted! Great job, Pesho!")
        break
    command = input()

if command == 'Tired!':
    diff = space_p - total_litres
    print(f"{round(diff)} quadratic m left.")


