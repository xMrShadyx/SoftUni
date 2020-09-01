budget = float(input())

cmd = input()

while cmd != "ACTION":
    salary = 0
    actor_name = str(cmd)
    if len(cmd) > 15:
        salary = budget * 0.2
    else:
        salary = float(input())
    budget -= salary
    if budget < 0:
        break
    cmd = input()

if budget < 0:
    print(f"We need {abs(budget):.2f} leva for our actors.")
else:
    print(f"We are left with {budget:.2f} leva.")