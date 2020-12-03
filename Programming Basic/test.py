N, X = input().strip()
N = int(N)
X = int(X)

count, total = 1, 0

while total >= 0:
    X = 2 * X
    count = count + 10
    if count == N:
        break
print(X)
print(N)
