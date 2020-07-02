import math

x = int(input())
y = float(input())
z = int(input())
workers = int(input())

total_grapes = x * y
wine = (0.4 * total_grapes) / 2.5
left_wine = wine - z
per_person = left_wine / workers

if wine > z:
    print(f"Good harvest this year! Total wine: {wine:.0f} liters.")
    print(f"{math.ceil(left_wine)} liters left -> {math.ceil(per_person)} liters per person.")
else:
    diff = z - wine
    print(f"It will be a tough winter! More {abs(diff):.0f} liters wine needed.")
