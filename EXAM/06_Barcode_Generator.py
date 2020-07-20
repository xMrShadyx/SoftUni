
#Ivailo Bonchev's Code  ################################################################################################
start_num = int(input())
end_num = int(input())
res_start = [int(x) for x in str(start_num)]
res_end = [int(x) for x in str(end_num)]

for i in range(start_num, end_num + 1):
    index = 0
    new_num = ""
    for j in str(i):
        if not int(j) % 2 == 0 and (res_start[index] <= int(j) <= res_end[index]):
            new_num = new_num + j
            index += 1
        else:
            index = 0
            new_num = ""
            break
        if len(new_num) == 4:
            print(f"{i} ", end="")

#JackBlaze's Code  #####################################################################################################
start_num_range = int(input())
end_num_range = int(input())

str_start_num = str(start_num_range)
str_end_num = str(end_num_range)

first_digit_start_num = int(str_start_num[0])
second_digit_start_num = int(str_start_num[1])
third_digit_start_num = int(str_start_num[2])
fourth_digit_start_num = int(str_start_num[3])

first_digit_end_num = int(str_end_num[0])
second_digit_end_num = int(str_end_num[1])
third_digit_end_num = int(str_end_num[2])
fourth_digit_end_num = int(str_end_num[3])

for curr_first_digit_to_check in range(first_digit_start_num, first_digit_end_num + 1):
    for curr_second_digit_to_check in range(second_digit_start_num, second_digit_end_num + 1):
        for curr_third_digit_to_check in range(third_digit_start_num, third_digit_end_num + 1):
            for curr_fourth_digit_to_check in range(fourth_digit_start_num, fourth_digit_end_num + 1):

                if curr_first_digit_to_check % 2 == 1 and curr_second_digit_to_check % 2 == 1 and curr_third_digit_to_check % 2 == 1 and curr_fourth_digit_to_check % 2 == 1:
                    print(f"{curr_first_digit_to_check}{curr_second_digit_to_check}{curr_third_digit_to_check}{curr_fourth_digit_to_check}", end=" ")


#Yanchev's Code  #######################################################################################################
first_num = int(input())
second_num = int(input())

first = str(first_num)
second = str(second_num)
for i in range(int(first[0]), int(second[0])+1):
   for j in range(int(first[1]), int(second[1])+1):
       for k in range(int(first[2]), int(second[2])+1):
           for l in range(int(first[3]), int(second[3])+1):
               if i % 2 != 0 and j % 2 != 0 and k % 2 != 0 and l % 2 != 0:
                   print(f"{i}{j}{k}{l}", end=" ")



#Emma's Code  #########################################################################################################
start = int(input())
end = int(input())

s1 = start // 1000 % 10
s2 = start // 100 % 10
s3 = start // 10 % 10
s4 = start % 10

e1 = end // 1000 % 10
e2 = end // 100 % 10
e3 = end // 10 % 10
e4 = end % 10

for d1 in range(s1, e1 + 1):
    if d1 % 2 != 0:
        for d2 in range(s2, e2 + 1):
            if d2 % 2 != 0:
                for d3 in range(s3, e3 + 1):
                    if d3 % 2 != 0:
                        for d4 in range(s4, e4 + 1):
                            if d4 % 2 != 0:
                                print(f"{d1}{d2}{d3}{d4}", end=' ')