budget = float(input())
video_cards = int(input())
processors = int(input())
ram = int(input())

price_video = video_cards * 250
price_processor = (price_video * 0.35) * processors
price_ram = (price_video * 0.10) * ram

total = price_video + price_processor + price_ram

if video_cards > processors:
    total = total * 0.85

last_total = abs(total - budget)

if total <= budget:
    print(f"You have {last_total:.2f} leva left!")
else:
    print(f"Not enough money! You need {last_total:.2f} leva more!")