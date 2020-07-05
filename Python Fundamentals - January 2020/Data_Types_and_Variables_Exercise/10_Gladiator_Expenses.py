lost_games = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

sum = 0
for game in range(1, lost_games + 1):
    
    if game % 2 == 0:
        sum += helmet_price
        
    if game % 3 == 0:
        sum += sword_price
        
    if game % 6 == 0:
        sum += shield_price
        
    if game % 12 == 0:
        sum += armor_price
        
print(f"Gladiator expenses: {sum} aureus")
        