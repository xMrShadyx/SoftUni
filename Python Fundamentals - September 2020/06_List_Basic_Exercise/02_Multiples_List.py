num1 = int(input())
num2 = int(input())

wierd_list = []

for i in range(1, num2 + 1):
    wierd_list.append(i * num1)
print(wierd_list)