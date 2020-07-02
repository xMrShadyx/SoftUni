w = float(input())
h = float(input())

w_to_cm = w * 100
h_to_cm = h * 100

rows = w_to_cm // 120

h_to_cm -= 100
buros_in_rows = h_to_cm // 70

all_buros = rows*buros_in_rows - 3
print(all_buros)