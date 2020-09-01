a1 = int(input())
a2 = int(input())
n = int(input())
n2 = n / 2

for i in range(a1, a2):
    if i % 2 != 0:
        for o in range(1, n):
            for p in range(1, int(n2)):
                if (o + p + i) % 2 != 0:
                    print(f"{chr(i)}-{o}{p}{i}")
