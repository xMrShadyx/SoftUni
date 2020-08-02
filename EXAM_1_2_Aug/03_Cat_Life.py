type_of_cat = input()
cat_sex = input()

life_of_a_pi = 0
is_valid = False

if type_of_cat == 'British Shorthair':
    if cat_sex == 'm':
        life_of_a_pi = (13 * 12) / 6
        print(f'{life_of_a_pi:.0f} cat months')
    else:
        life_of_a_pi = (14 * 12) / 6
        print(f'{life_of_a_pi:.0f} cat months')

elif type_of_cat == 'Siamese':
    if cat_sex == 'm':
        life_of_a_pi = (15 * 12) / 6
        print(f'{life_of_a_pi:.0f} cat months')
    else:
        life_of_a_pi = (16 * 12) / 6
        print(f'{life_of_a_pi:.0f} cat months')

elif type_of_cat == 'Persian':
    if cat_sex == 'm':
        life_of_a_pi = (14 * 12) / 6
        print(f'{life_of_a_pi:.0f} cat months')
    else:
        life_of_a_pi = (15 * 12) / 6
        print(f'{life_of_a_pi:.0f} cat months')

elif type_of_cat == 'Ragdoll':
    if cat_sex == 'm':
        life_of_a_pi = (16 * 12) / 6
        print(f'{life_of_a_pi:.0f} cat months')
    else:
        life_of_a_pi = (17 * 12) / 6
        print(f'{life_of_a_pi:.0f} cat months')

elif type_of_cat == 'American Shorthair':
    if cat_sex == 'm':
        life_of_a_pi = (12 * 12) / 6
        print(f'{life_of_a_pi:.0f} cat months')
    else:
        life_of_a_pi = (13 * 12) / 6
        print(f'{life_of_a_pi:.0f} cat months')

elif type_of_cat == 'Siberian':
    if cat_sex == 'm':
        life_of_a_pi = (11 * 12) / 6
        print(f'{life_of_a_pi:.0f} cat months')
    else:
        life_of_a_pi = (12 * 12) / 6
        print(f'{life_of_a_pi:.0f} cat months')
else:
    print(f'{type_of_cat} is invalid cat!')



