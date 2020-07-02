# 1. x – височината на къщата – реално число в интервала [2...100]
x = float(input())
# 2. y – дължината на страничната стена – реално число в интервала [2...100]
y = float(input())
# 3. h – височината на триъгълната стена на прокрива – реално число в интервала [2...100]
h = float(input())


side_wall = x * y
window = 1.5 * 1.5
two_sides = 2 * side_wall - 2 * window
back_wall = x * x
entrance = 1.2 * 2
back_and_front = 2 * back_wall - entrance
total_space = two_sides + back_and_front
total_g_paint = total_space / 3.4

#roof
two_squares = 2 * ( x * y)
two_rectangls = 2 * ( x * h ) / 2
total_roof = two_squares + two_rectangls
total_r_paint = total_roof / 4.3

print(f"{total_g_paint:.2f}")
print(f"{total_r_paint:.2f}")