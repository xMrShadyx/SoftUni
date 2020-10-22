number = input().split(".")

num1 = int(number[0])
num2 = int(number[1])
num3 = int(number[2])


if num3 == 9:
	num3 = 0
	num2 += 1
else:
	num3 += 1

if num2 > 9:
	num2 = 0
	if num1 != 9:
		num1 += 1

if num1 == 10:
	num1 = 0
print(f"{num1}.{num2}.{num3}")