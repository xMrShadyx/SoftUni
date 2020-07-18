movie_name = input()
amount_days = int(input())
amount_tickets = int(input())
price_tickets = float(input())
percent_theater = int(input())

daily_sold_tickets = (amount_tickets * price_tickets) * amount_days
left_percent = (daily_sold_tickets * percent_theater) / 100
total = daily_sold_tickets - left_percent

print(f"The profit from the movie {movie_name} is {total:.2f} lv.")
