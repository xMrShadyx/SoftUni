import math
amount_people = int(input())
money_per_person = float(input())
money_per_bed = float(input())
money_per_umbrella = float(input())


taksa = amount_people * money_per_person
less_people = math.ceil(amount_people * 0.75) * money_per_bed
less_bed_people = math.ceil(amount_people * 0.50) * money_per_umbrella

total = taksa + less_people + less_bed_people

print(f"{total:.2f} lv.")