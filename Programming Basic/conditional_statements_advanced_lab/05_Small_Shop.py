article = input()
town = input()
amount = float(input())

price = 0

if article == 'coffee':
    if town == 'Sofia':
        price = 0.5
    if town == 'Plovdiv':
        price = 0.4
    if town == 'Varna':
        price = 0.45
elif article == 'water':
    if town == 'Sofia':
        price = 0.8
    if town == 'Plovdiv':
        price = 0.7
    if town == 'Varna':
        price = 0.7
elif article == 'beer':
    if town == 'Sofia':
        price = 1.2
    if town == 'Plovdiv':
        price = 1.15
    if town == 'Varna':
        price = 1.1
elif article == 'sweets':
    if town == 'Sofia':
        price = 1.45
    if town == 'Plovdiv':
        price = 1.3
    if town == 'Varna':
        price = 1.35
elif article == 'peanuts':
    if town == 'Sofia':
        price = 1.6
    if town == 'Plovdiv':
        price = 1.5
    if town == 'Varna':
        price = 1.55

total = amount * price

print(total)