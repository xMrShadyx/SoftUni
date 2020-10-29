ppl_w8_for_lift = int(input())
state_of_lift = [int(el) for el in input().split()]

position = 0

while True:
	if position >= len(state_of_lift):
		break
	if ppl_w8_for_lift == 0:
		break

	if state_of_lift[position] != 4:
		state_of_lift[position] += 1
		ppl_w8_for_lift -= 1
	else:
		position += 1

total = 0

for item in state_of_lift:
	total += item

if ppl_w8_for_lift == 0 and len(state_of_lift) * 4 == total:
	print(" ".join([str(el) for el in state_of_lift]))
elif ppl_w8_for_lift == 0:
	print("The lift has empty spots!")
	print(" ".join([str(el) for el in state_of_lift]))
else:
	print(f"There isn't enough space! {ppl_w8_for_lift} people in a queue!")
	print(" ".join([str(el) for el in state_of_lift]))
