number_range = int(input())

pos_list = []
neg_list = []
count_neg = 0
for i in range(1, number_range + 1):
    number_to_list = int(input())
    if number_to_list >= 0:
        pos_list.append(number_to_list)
    else:
        neg_list.append(number_to_list)

len_pos = len(pos_list)
count_neg = sum(neg_list)

print(pos_list)
print(neg_list)
print(f' Count of positive: {len_pos}. Sum of negatives: {count_neg}')
