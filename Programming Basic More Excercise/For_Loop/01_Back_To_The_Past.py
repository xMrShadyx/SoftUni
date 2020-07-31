heritage = float(input())
year = int(input())

age = 17
spending = 0

for i in range(1800, year + 1):
    age += 1
    if i % 2 == 0:
        spending += 12000
    else:
        spending += 12000 + 50 * age

diff = abs(heritage - spending)
if spending > heritage:
    print(f"He will need {diff:.2f} dollars to survive.")
else:
    print(f"Yes! He will live a carefree life and will have {diff:.2f} dollars left.")