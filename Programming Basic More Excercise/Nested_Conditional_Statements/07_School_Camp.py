season = input()
group_gender = input()
amount_students = int(input())
amount_nights = int(input())

price = 0
sport_type = ''

if season == 'Winter':
    if group_gender == 'boys' or group_gender == 'girls':
        price = 9.6
    elif group_gender == 'mixed':
        price = 10
elif season == 'Spring':
    if group_gender == 'boys' or group_gender == 'girls':
        price = 7.2
    elif group_gender == 'mixed':
        price = 9.5
elif season == 'Summer':
    if group_gender == 'boys' or group_gender == 'girls':
        price = 15
    elif group_gender == 'mixed':
        price = 20

if season == 'Winter':
    if group_gender == 'girls':
        sport_type = 'Gymnastics'
    elif group_gender == 'boys':
        sport_type = 'Judo'
    elif group_gender == 'mixed':
        sport_type = 'Ski'

elif season == 'Spring':
    if group_gender == 'girls':
        sport_type = 'Athletics'
    elif group_gender == 'boys':
        sport_type = 'Tennis'
    elif group_gender == 'mixed':
        sport_type = 'Cycling'

elif season == 'Summer':
    if group_gender == 'girls':
        sport_type = 'Volleyball'
    elif group_gender == 'boys':
        sport_type = 'Football'
    elif group_gender == 'mixed':
        sport_type = 'Swimming'

total_price = amount_nights * price * amount_students

if 10 <= amount_students < 20:
    total_price = total_price * 0.95
elif 20 <= amount_students < 50:
    total_price = total_price * 0.85
elif amount_students >= 50:
    total_price = total_price * 0.50

print(f"{sport_type} {total_price:.2f} lv.")