n1 = 3
n2 = 5
n3 = 5

n1_current = 0
n2_current = 0
n3_current = 0

for x1 in range(1, n1 + 1):
    if x1 % 2 == 0:
        n1_current = x1
        for x2 in range(1, n2 + 1):
            if x2 % 2 == 1:
                n2_current = x2
                for x3 in range(1, n3 + 1):
                    if x3 % 2 == 0:
                        n3_current = x3

                    print(f'{n1_current} {n2_current} {n3_current}')
