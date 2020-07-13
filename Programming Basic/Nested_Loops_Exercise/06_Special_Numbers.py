n = int(input())

for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            for l in range(1, 10):
                if (n % i == 0) and (n % j == 0) and (n % k == 0) and (n % l == 0):
                    print(f"{i}{j}{k}{l}", end=" ")