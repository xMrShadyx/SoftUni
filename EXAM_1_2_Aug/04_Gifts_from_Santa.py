n = int(input())
m = int(input())
s = int(input())

for i in range(m + 1, n - 1, -1):
    if i % 2 == 0 and i % 3 == 0:
        if i == s:
            break
        else:
            print(i, end=' ')
