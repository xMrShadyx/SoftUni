cards = input()
shuffles = int(input())
deck = cards.split()

before_shuffle = deck
after_shuffle = []

for i in range(shuffles):
	after_shuffle = []
	for j in range(len(deck) // 2):
		after_shuffle.append(before_shuffle[j])
		after_shuffle.append(before_shuffle[j + len(deck) // 2])
	before_shuffle = after_shuffle

print(after_shuffle)