import math
movie_name = input()
movie_length = int(input())
break_length = int(input())

time_for_lunch = break_length / 8
time_for_rest = break_length / 4
time_left = break_length - time_for_lunch - time_for_rest

if time_left >= movie_length:
    diff = math.ceil(time_left - movie_length)
    print(f"You have enough time to watch {movie_name} and left with {diff} minutes free time.")
else:
    diff1 = math.ceil(movie_length - time_left)
    print(f"You don't have enough time to watch {movie_name}, you need {diff1} more minutes.")