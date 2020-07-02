temperature = float(input())
time = input()

Outfit = ""
Shoes = ""

if 10 <= temperature <= 18:
    if time == 'Morning':
        Outfit = 'Sweatshirt'
        Shoes = 'Sneakers'
        print(f"It's {temperature:.0f} degrees, get your {Outfit} and {Shoes}.")
    elif time == 'Afternoon':
        Outfit = 'Shirt'
        Shoes = 'Moccasins'
        print(f"It's {temperature:.0f} degrees, get your {Outfit} and {Shoes}.")
    elif time == 'Evening':
        Outfit = 'Shirt'
        Shoes = 'Moccasins'
        print(f"It's {temperature:.0f} degrees, get your {Outfit} and {Shoes}.")
elif 18 < temperature <= 24:
    if time == 'Morning':
        Outfit = 'Shirt'
        Shoes = 'Moccasins'
        print(f"It's {temperature:.0f} degrees, get your {Outfit} and {Shoes}.")
    elif time == 'Afternoon':
        Outfit = 'T-Shirt'
        Shoes = 'Sandals'
        print(f"It's {temperature:.0f} degrees, get your {Outfit} and {Shoes}.")
    elif time == 'Evening':
        Outfit = 'Shirt'
        Shoes = 'Moccasins'
        print(f"It's {temperature:.0f} degrees, get your {Outfit} and {Shoes}.")
elif temperature >= 25:
    if time == 'Morning':
        Outfit = 'T-Shirt'
        Shoes = 'Sandals'
        print(f"It's {temperature:.0f} degrees, get your {Outfit} and {Shoes}.")
    elif time == 'Afternoon':
        Outfit = 'Swim Suit'
        Shoes = 'Barefoot'
        print(f"It's {temperature:.0f} degrees, get your {Outfit} and {Shoes}.")
    elif time == 'Evening':
        Outfit = 'Shirt'
        Shoes = 'Moccasins'
        print(f"It's {temperature:.0f} degrees, get your {Outfit} and {Shoes}.")
