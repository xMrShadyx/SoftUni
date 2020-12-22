<<<<<<< HEAD
def solution(raw_data):
	data = raw_data.split(" ")
	result = {}
	for i in range(0, len(data), 2):
		key = data[i]
		value = data[i + 1]
		result[key] = int(value)
	return result


def solution_comprehension(raw_data):
	data = raw_data.split(" ")
	return {data[i]: int(data[i + 1]) for i in range(0, len(data), 2)}


# raw_data = 'bread 10 butter 4 sugar 9 jam 12'
# print(solution(input()))
# print(solution_comprehension(input()))


# My code with out looking:
def solve(raw_data):
	data = raw_data.split(" ")
	result = {}
	for i in range(0, len(data), 2):
		key = data[i]
		value = data[i + 1]
		result[key] = int(value)
	return result


raw_data = 'bread 10 butter 4 sugar 9 jam 12'
=======
def solution(raw_data):
	data = raw_data.split(" ")
	result = {}
	for i in range(0, len(data), 2):
		key = data[i]
		value = data[i + 1]
		result[key] = int(value)
	return result


def solution_comprehension(raw_data):
	data = raw_data.split(" ")
	return {data[i]: int(data[i + 1]) for i in range(0, len(data), 2)}


# raw_data = 'bread 10 butter 4 sugar 9 jam 12'
# print(solution(input()))
# print(solution_comprehension(input()))


# My code with out looking:
def solve(raw_data):
	data = raw_data.split(" ")
	result = {}
	for i in range(0, len(data), 2):
		key = data[i]
		value = data[i + 1]
		result[key] = int(value)
	return result


raw_data = 'bread 10 butter 4 sugar 9 jam 12'
>>>>>>> 06f2e621b68de7dbe64b4c1441e71917f616ece7
print(solve(raw_data))