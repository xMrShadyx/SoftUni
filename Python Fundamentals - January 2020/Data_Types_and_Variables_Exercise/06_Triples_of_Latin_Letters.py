n = int(input())

for i in range(n):
    for j in range(n):
        for k in range(n):
            char_one = chr(97 + i)
            char_two = chr(97 + j)
            char_three = chr(97 + k)
            print(f"{char_one}{char_two}{char_three}")