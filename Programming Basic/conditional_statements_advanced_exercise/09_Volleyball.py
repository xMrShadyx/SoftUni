import math
type_of_year = input() #leap or normal
amount_holidays = int(input()) #weekends not included
amount_weekends = int(input())

total_games = 0
week_in_year = 48

if type_of_year == 'normal':
    weekends_in_sofia = week_in_year - amount_weekends
    games_in_sofia = weekends_in_sofia * 3/4
    own_town = amount_holidays * 2/3
    total_games = games_in_sofia + amount_weekends + own_town
    print(math.floor(total_games))

elif type_of_year == 'leap':
    weekends_in_sofia = week_in_year - amount_weekends
    games_in_sofia = weekends_in_sofia * 3/4
    own_town = amount_holidays * 2/3
    total_games = games_in_sofia + amount_weekends + own_town
    total_n_games = total_games * 0.15
    total_games = total_n_games + total_games
    print(math.floor(total_games))