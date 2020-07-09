import sys

def read_number_list():
    input_arr = input()
    nums = []
    for i in input_arr:
        nums.append(int(i))
    return nums


def exchange(nums, index):
    new_lsit = []
    for i in range(index + 1, len(nums)):
        new_lsit.append(nums[i])
    for i in range(index + 1):
        new_lsit.append(nums[i])
    return new_lsit

def max_number_index(nums, type):
    max_num = -sys.maxsize
    max_num_index = -1
    if type == 'even':
        for i in range(len(nums)):
            num = nums[i]
            if num % 2 == 0 and num >= max_num:
                max_num = num
                max_num_index = i
    else:
        for i in range(len(nums)):
            num = nums[i]
            if num % 2 != 0 and num >= max_num:
                max_num = num
                max_num_index = i
    return max_num_index

def solve():
    nums = read_number_list()
    command_input = input()
    while command_input != 'end':
        args = command_input.split()
        command = args[0]
        if command == 'exchange':
            index = int(args[1])
            if index < 0 or index >= len(nums):
                print("Invalid index")
                command_input = input()
                continue
            nums = exchange(nums, index)
        elif command == "max":
            type = args[1]
            max_index = max_number_index(nums, type)
            pass
        command_input = input()


solve()