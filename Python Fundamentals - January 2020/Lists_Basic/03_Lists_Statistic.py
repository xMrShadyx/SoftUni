n = int(input())

positives = []
negatives = []

for _ in range(n):
    current_number = int(input())
    if current_number >= 0:
        positives.append(current_number)
    else:
        negatives.append(current_number)

print(positives)
print(negatives)
print(f"Count of positive: {len(positives)}, Sum of negatives {sum(negatives)}")