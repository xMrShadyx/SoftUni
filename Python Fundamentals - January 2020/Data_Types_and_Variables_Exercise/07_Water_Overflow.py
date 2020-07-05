n = int(input())

capacity = 255

for i in range(n):
    litres = int(input())

    if capacity - litres < 0:
        print("Insufficient capacity!")
    else:
        capacity -= litres

print(255 - capacity)
