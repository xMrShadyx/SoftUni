positions_alphabet = {chr(ele + 97): ele + 1 for ele in range(26)}

data = input().split()
result = 0

for el in data:
	first_letter = el[0]
	last_letter = el[-1]
	number = int(el[1:-1])
	if first_letter.isupper():
		number /= positions_alphabet[first_letter.lower()]
	elif first_letter.islower():
		number *= positions_alphabet[first_letter]

	if last_letter.isupper():
		number -= positions_alphabet[last_letter.lower()]
	elif last_letter.islower():
		number += positions_alphabet[last_letter]

	result += number

print(f"{result:.2f}")
