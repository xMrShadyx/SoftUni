movie_name = input()
room_type = input()
amount_tickets = int(input())

price = 0

if movie_name == 'A Star Is Born':
    if room_type == 'normal':
        price = 7.5
    elif room_type == 'luxury':
        price = 10.50
    elif room_type == 'ultra luxury':
        price = 13.50
elif movie_name == 'Bohemian Rhapsody':
    if room_type == 'normal':
        price = 7.35
    elif room_type == 'luxury':
        price = 9.45
    elif room_type == 'ultra luxury':
        price = 12.75
elif movie_name == 'Green Book':
    if room_type == 'normal':
        price = 8.15
    elif room_type == 'luxury':
        price = 10.25
    elif room_type == 'ultra luxury':
        price = 13.25
elif movie_name == 'The Favourite':
    if room_type == 'normal':
        price = 8.75
    elif room_type == 'luxury':
        price = 11.55
    elif room_type == 'ultra luxury':
        price = 13.95

total_tickets = price * amount_tickets

print(f"{movie_name} -> {total_tickets:.2f} lv.")