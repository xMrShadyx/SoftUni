single_string = input().split(', ')
number_of_beggars = int(input())

simple_beggars = single_string
simple_list = [0] * number_of_beggars

# TODO: IF Beggars == to amount of strings
if len(simple_list) == len(simple_beggars):
    simple_list = simple_beggars

# TODO: IF Beggars more than strings...
elif len(simple_beggars) < len(simple_list):
    simple_list = simple_beggars
    x = len(simple_beggars) - len(simple_list)
    for i in range(x + 1):
        simple_list.append('0')

# TODO: IF Beggars are less than stings


# TODO: STR -> INT
for i in range(0, len(simple_list)):
    simple_list[i] = int(simple_list[i])
print(simple_list)
