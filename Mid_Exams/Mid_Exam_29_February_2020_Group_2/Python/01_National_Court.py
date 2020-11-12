first = int(input())
second = int(input())
third = int(input())
people_count = int(input())

hours = 0
all_people = first + second + third
while people_count > 0:
	hours += 1
	people_count -= all_people
	if hours % 4 == 0:
		hours += 1
print(f"Time needed: {hours}h.")