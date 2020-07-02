from math import pi

shape = input()

if shape == "square":
    area = float(input())
    area = area * area
    print(f"{area:.3f}")

elif shape == "rectangle":
    area1 = float(input())
    area2 = float(input())
    area = area1 * area2
    print(f"{area:.3f}")

elif shape == "circle":
    radius = float(input())
    radius1 = (radius * radius) * pi
    print(f"{radius1:.3f}")

elif shape == "triangle":
    side1 = float(input())
    side2 = float(input())
    area = (side1 * side2) / 2
    print(f"{area:.3f}")