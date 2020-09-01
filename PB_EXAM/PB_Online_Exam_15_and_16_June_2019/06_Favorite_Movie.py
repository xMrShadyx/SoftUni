import sys

cmd = input()
movies = 0

biggest = -sys.maxsize
points = 0

while cmd != "STOP":
    movies += 1
    movie_names = str(cmd)
    movie_len = len(movie_names)
    for i in movie_names:
        if i.isupper():
            points += ord(i) - movie_len
        elif i.islower():
            points += ord(i) - (movie_len * 2)
        else:
            points += ord(i)

    if points > biggest:
        biggest = points
        actual_name = movie_names
    points = 0
    if movies == 7:
        break
    else:
        cmd = input()

if cmd == "STOP":
    print(f"The best movie for you is {actual_name} with {biggest} ASCII sum.")
else:
    print("The limit is reached.")
    print(f"The best movie for you is {actual_name} with {biggest} ASCII sum.")