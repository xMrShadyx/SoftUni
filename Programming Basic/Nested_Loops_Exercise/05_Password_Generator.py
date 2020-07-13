n = int(input())
l = int(input())

for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(97, 97 + l):
            for v in range(97, 97 + l):
                for m in range(1, n + 1):
                    if m > i and m > j:
                        print(f"{i}{j}{chr(k)}{chr(v)}{m}", end=" ")