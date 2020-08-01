num_of_detergent = int(input())
detergent_in_ml = num_of_detergent * 750
dishes = 0
pots = 0
count_num = 0
count_dishes = 0
count_pots = 0

line = input()
while line != 'End':
    count_num += 1
    if count_num % 3 == 0:
        pots = int(line)
        count_pots += pots
        detergent_in_ml -= pots * 15

    else:
        dishes = int(line)
        count_dishes += dishes
        detergent_in_ml -= dishes * 5
    if detergent_in_ml < 0:
        print(f'Not enough detergent, {abs(detergent_in_ml)} ml. more necessary!')
        break
    line = input()

if detergent_in_ml >= 0:
    print('Detergent was enough!')
    print(f'{count_dishes} dishes and {count_pots} pots were washed.')
    print(f'Leftover detergent {detergent_in_ml} ml.')