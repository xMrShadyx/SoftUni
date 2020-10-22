n = int(input())

free_chairs = 0
room = 0
negative = 0

for _ in range(n):
	room += 1
	n_lines = input().split()

	chairs = len(n_lines[0])
	free = int(n_lines[1])
	if chairs < free:
		print(f"{free - chairs} more chairs needed in room {room}")
		negative += 1
	else:
		free_chairs += chairs - free

if negative == 0:
	print(f"Game On, {free_chairs} free chairs left")