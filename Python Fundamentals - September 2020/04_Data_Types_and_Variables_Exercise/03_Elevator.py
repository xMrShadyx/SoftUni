from math import ceil

persons = int(input())
capacity = int(input())

result = persons / capacity

print(f"{ceil(result)}")