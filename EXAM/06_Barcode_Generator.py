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