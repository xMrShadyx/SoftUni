numbers = input().split()
number_of_removals = int(input())
the_numbers = [int(number) for number in numbers]
temp_numbs = []

while number_of_removals:
	sorted_numbers = the_numbers
	sorted_numbers.sort(reverse=True)
	temp_numbs.append(sorted_numbers.pop(-1))
	number_of_removals -= 1

fkin_numbers = [int(number) for number in numbers]

for i in fkin_numbers:
	for j in temp_numbs:
		if int(j) in fkin_numbers:
			fkin_numbers.remove(j)

print(fkin_numbers)