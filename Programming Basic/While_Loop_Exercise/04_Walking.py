goal = 10000

total_steps = 0

while total_steps < goal:
    line = input()
    if line == 'Going home':
        steps_home = int(input())
        total_steps += steps_home
        if total_steps < goal:
            diff = goal - total_steps
            print(f"{diff} more steps to reach goal.")
        break

    steps = int(line)
    total_steps += steps

    if total_steps >= goal:
        break

if total_steps >= goal:
    print(f"Goal reached! Good job!")
    diff = total_steps - goal
    print(f"{diff} steps over the goal!")

