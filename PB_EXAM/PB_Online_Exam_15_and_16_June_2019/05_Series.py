budget = float(input())
amount_series = int(input())

price = 0

for i in range(amount_series):
    series_name = input()
    series_price = float(input())
    t = series_price
    if series_name == 'Thrones':
        price += series_price * 0.5
    elif series_name == 'Lucifer':
        price += series_price * 0.6
    elif series_name == 'Protector':
        price += series_price * 0.7
    elif series_name == 'TotalDrama':
        price += series_price * 0.8
    elif series_name == 'Area':
        price += series_price * 0.9
    else:
        price += series_price

if budget >= price:
    diff = budget - price
    print(f"You bought all the series and left with {diff:.2f} lv.")
else:
    diff1 = price - budget
    print(f"You need {diff1:.2f} lv. more to buy the series!"
)