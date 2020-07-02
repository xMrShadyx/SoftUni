import sys
n = int(input())

current_max = -sys.maxsize
current_min = sys.maxsize


for i in range(n):
    number = int(input())
    if number > current_max:
        current_max = number
    if number < current_min:
        current_min = number

print(f'Max number: {current_max}')
print(f'Min number: {current_min}')