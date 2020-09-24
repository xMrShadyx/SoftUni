str_one = input()
str_two = input()

for i in range(len(str_one)):
    if str_one[i] != str_two[i]:
        for str_two_index in range(0, i + 1):
            print(str_two[str_two_index], end="")

        for str_one_index in range(i + 1, len(str_one)):
            print(str_one[str_one_index], end="")
        print()
