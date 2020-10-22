# result = [print(item, end="") for item in input().split()[::-1]]


text = input().split()

for item in sorted(text)[::-1]:
	print(item, end="")

