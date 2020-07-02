# •	На първия ред е месецът – May, June, July, August, September или October;
# •	На втория ред е броят на нощувките – цяло число.

month = input()
nights = int(input())

studio_price = 0
apartment_price = 0

# Май и октомври	      Юни и септември	             Юли и август
# Студио – 50 лв.      /нощувка	Студио – 75.20 лв.      /нощувка	Студио – 76 лв./нощувка
# Апартамент – 65 лв. /нощувка	Апартамент – 68.70 лв.  /нощувка	Апартамент – 77 лв./нощувка


if month == 'May' or month == 'October':
    studio_price = 50
    apartment_price = 65
    if nights > 7 and nights <= 13:
        studio_price *= 0.95  #47.5
    if nights >= 14:
        studio_price *= 0.70 #35
        apartment_price = apartment_price * 0.9 #58.5
elif month == 'June' or month == 'September':
    studio_price = 75.20
    apartment_price = 68.70
    if nights > 14:
        studio_price *= 0.80 #60.16
        apartment_price *= 0.90 #61.83
elif month == 'July' or month == 'August':
    studio_price = 76
    apartment_price = 77
    if nights > 14:
        apartment_price *= 0.90  #69.3


total_studio_price = studio_price * nights
total_apartment_price = apartment_price * nights


print(f'Apartment: {total_apartment_price:.2f} lv.')
print(f'Studio: {total_studio_price:.2f} lv.')