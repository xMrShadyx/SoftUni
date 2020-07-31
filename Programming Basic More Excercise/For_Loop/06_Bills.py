months = int(input())
av_months = 0
el_money = 0
water_money = 0
internet_money = 0
other_money = 0

for i in range(months):
    el1_money = 0
    water1_money = 0
    int1_money = 0
    bills = float(input())
    av_months += 1
    el_money += bills
    el1_money += bills
    water_money += 20
    water1_money += 20
    internet_money += 15
    int1_money += 15
    total_money = el1_money + water1_money + int1_money
    other_money += ((el1_money + water1_money + int1_money) * 0.2) + total_money

monthly_avr = (el_money + water_money + internet_money + other_money) / av_months

print(f'Electricity: {el_money:.2f} lv')
print(f'Water: {water_money:.2f} lv')
print(f'Internet: {internet_money:.2f} lv')
print(f'Other: {other_money:.2f} lv')
print(f'Average: {monthly_avr:.2f} lv')
