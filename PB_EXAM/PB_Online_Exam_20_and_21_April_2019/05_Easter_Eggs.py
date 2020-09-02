import sys

egg_amount = int(input())

red = 0
orange = 0
blue = 0
green = 0

max1 = 0
color = ''

for i in range(egg_amount):
    eggs_color = input()
    if eggs_color == 'red':
        red += 1
    elif eggs_color == 'orange':
        orange += 1
    elif eggs_color == 'blue':
        blue += 1
    elif eggs_color == 'green':
        green += 1

#BIGGEST OF FOUR COLORS
if (red >= orange) and (red >= blue) and (red >= green):
    max1 = red
    color = 'red'
elif (orange >= red) and (orange >= green) and (orange >= blue):
    max1 = orange
    color = 'orange'
elif (green >= red) and (green >= blue) and (green >= orange):
    max1 = green
    color = 'green'
else:
    max1 = blue
    color = 'blue'

print(f"Red eggs: {red}")
print(f"Orange eggs: {orange}")
print(f"Blue eggs: {blue}")
print(f"Green eggs: {green}")
print(f"Max eggs: {max1} -> {color}")