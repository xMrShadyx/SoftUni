import re
pattern = r'^(@#|@#+)[A-Z][A-Za-z0-9]{4,}[A-Z]($@#|@#+)'
# pattern = r'@#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+'

n = int(input())

for _ in range(n):
	barcode_line = input()
	if re.match(pattern, barcode_line):
		digits = re.findall(r'\d', barcode_line)
		if digits:
			print(f"Product group: {''.join(digits)}" )
		else:
			print("Product group: 00")
	else:
		print("Invalid barcode")
