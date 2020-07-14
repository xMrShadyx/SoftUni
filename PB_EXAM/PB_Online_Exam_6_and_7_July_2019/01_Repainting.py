needed_plastic_cover = int(input())
needed_paint = int(input())
needed_liquid = int(input())
needed_hours = int(input())

plastic_cover = (needed_plastic_cover + 2) * 1.5
paint = ((needed_paint * 0.10) + needed_paint) * 14.50
liquid = needed_liquid * 5

total = plastic_cover + paint + liquid + 0.40
payment = (total * 0.30) * needed_hours

last_total = total + payment

print(f"Total expenses: {last_total:.2f} lv.")
