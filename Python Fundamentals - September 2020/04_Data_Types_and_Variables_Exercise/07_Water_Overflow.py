n = int(input())
tank_capacity = 0

for i in range(n):
    water = int(input())
    tank_capacity += water
    if tank_capacity > 255:
        tank_capacity -= water
        print("Insufficient capacity!")

print(f"{tank_capacity}")
