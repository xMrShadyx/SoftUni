import math
n = int(input())
time = input()

if n < 20:
    if time == "day":
        total = 0.7 + n * 0.79
        print(f"{total:.2f}")
    else:
        total = 0.7 + n * 0.9
        print(f"{total:.2f}")
if n >= 20 and n < 100:
    total = n * 0.09
    print(f"{total:.2f}")
if n > 100:
    total = n * 0.06
    print(f"{total:.2f}")