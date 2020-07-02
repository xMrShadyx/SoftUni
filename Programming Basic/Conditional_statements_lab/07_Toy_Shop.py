travel = float(input())
puzzles = int(input())
talking_doll = int(input())
teddy_bears = int(input())
minions = int(input())
trucks = int(input())

price_puzzle = puzzles * 2.6
price_talking_doll = talking_doll * 3
price_teddy_bears = teddy_bears * 4.1
price_minions = minions * 8.2
price_trucks = trucks * 2

tt_price = price_puzzle + price_talking_doll + price_teddy_bears + price_minions + price_trucks
tt_count = puzzles + talking_doll + teddy_bears + minions + trucks

# print(tt_count)
# print(tt_price)

if tt_count >= 50:
    tt_price = tt_price * 0.75

rent = tt_price * 0.90

# print(rent)

if rent >= travel:
    left_money = rent - travel
    print(f"Yes! {left_money:.2f} lv left.")
else:
    needed_money = travel - rent
    print(f"Not enough money! {needed_money:.2f} lv needed.")
