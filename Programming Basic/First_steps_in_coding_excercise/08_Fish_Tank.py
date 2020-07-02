# От конзолата се четат 4 реда:
# ⦁	Дължина в см – цяло число
lenght = float(input())
# ⦁	Широчина в см – цяло число
width = float(input())
# ⦁	Височина в см – цяло число
hight = float(input())
# ⦁	Процент зает обем – реално число
some_text = float(input())


aquarium_capacity = lenght * width * hight
some_percent = some_text * 0.01

needed_litres = aquarium_capacity * (1 - some_percent)
needed_litres = needed_litres * 0.001

print(needed_litres)