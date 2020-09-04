amount_of_movies = int(input())

current_movie = 0
highest_movie = 0
highest_name = ''
lowest_movie = 1000
lowest_name = ''
avr_rating = 0

for i in range(amount_of_movies):
    movie_name = input()
    movie_rating = float(input())
    avr_rating += movie_rating
    current_movie = movie_rating
    if movie_rating > highest_movie:
        highest_movie = movie_rating
        highest_name = movie_name
    elif current_movie < lowest_movie:
        lowest_movie = current_movie
        lowest_name = movie_name

print(f"{highest_name} is with highest rating: {highest_movie}")
print(f"{lowest_name} is with lowest rating: {lowest_movie}")
print(f"Average rating: {(avr_rating / amount_of_movies):.1f}")

