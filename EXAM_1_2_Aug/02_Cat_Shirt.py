hand_size = float(input())
front_size = float(input())
type_of_mats = input()
necktie_needed = input()

first_price = (hand_size * 2) + (front_size * 2)
second_price = ((first_price * 0.1) + first_price) / 100

another_price = 0


if type_of_mats == 'Linen':
    another_price = (second_price * 15) + 10
elif type_of_mats == 'Cotton':
    another_price = (second_price * 12) + 10
elif type_of_mats == 'Denim':
    another_price = (second_price * 20) + 10
elif type_of_mats == 'Twill':
    another_price = (second_price * 16) + 10
elif type_of_mats == 'Flannel':
    another_price = (second_price * 11) + 10

if necktie_needed == 'Yes':
    another_price = another_price * 1.2
    print(f'The price of the shirt is: {another_price:.2f}lv.')
else:
    print(f'The price of the shirt is: {another_price:.2f}lv.')