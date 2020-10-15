def loading_bar(n):
    list_n = '[..........]'
    for i in list_n:
        i = list_n.replace('.', '%', int(n))

    if n < 10:
        return f"{int(n * 10)}% {i} \nStill loading..."
    else:
        return f"{int(n * 10)}% Complete! \n{i}"


number = 5
print(loading_bar(number))
