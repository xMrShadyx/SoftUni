season = input()
km_per_month = float(input())

lv_per_km = 0

if km_per_month <= 5000:
    if season == 'Spring' or season == 'Autumn':
        lv_per_km = 0.75
    elif season == 'Summer':
        lv_per_km = 0.90
    elif season == 'Winter':
        lv_per_km = 1.05

elif 5000 < km_per_month <= 10000:
    if season == 'Spring' or season == 'Autumn':
        lv_per_km = 0.95
    elif season == 'Summer':
        lv_per_km = 1.10
    elif season == 'Winter':
        lv_per_km = 1.25

elif 10000 < km_per_month <= 20000:
    if season == 'Spring' or season == 'Autumn':
        lv_per_km = 1.45
    elif season == 'Summer':
        lv_per_km = 1.45
    elif season == 'Winter':
        lv_per_km = 1.45

total = ((lv_per_km * km_per_month) * 4) * 0.90

print(f"{total:.2f}")
