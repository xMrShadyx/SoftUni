am_chicken_menu = int(input())
am_fish_menu = int(input())
am_vegi_menu = int(input())

chicken_menu = 10.35
fish_menu = 12.40
vegi_menu = 8.15

t1 = am_chicken_menu * chicken_menu
t2 = am_fish_menu * fish_menu
t3 = am_vegi_menu * vegi_menu

total_recipe = t1 + t2 + t3
deser_price = total_recipe * 0.2
last_recipe = deser_price + total_recipe + 2.5
print(f"Total: {last_recipe:.2f}")
