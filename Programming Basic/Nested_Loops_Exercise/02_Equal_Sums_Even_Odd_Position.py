first_num = int(input())
second_num = int(input())

for i in range(first_num, second_num + 1):
    num_as_string = str(i)

    odd_sum = 0
    even_sum = 0
    for index, symbol in enumerate(num_as_string):
        if index % 2 == 0:
            even_sum += int(symbol)
        else:
            odd_sum += int(symbol)

    if odd_sum == even_sum:
        print(num_as_string, end=" ")