screen_type = input()
rows = int(input())
colums = int(input())

Premiere = 12
Normal = 7.5
Discount = 5

cinema_capacity = rows * colums
income = 0

if screen_type == 'Premiere':
    income = cinema_capacity * Premiere
elif screen_type == 'Normal':
    income = cinema_capacity * Normal
elif screen_type == 'Discount':
    income = cinema_capacity * Discount

print(f'{income:.2f} leva')