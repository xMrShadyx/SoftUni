is_valid = True

while not False:
    number = float(input())
    if number >= 0:
        print(f"Result: {number * 2:.2f}")
    else:
        print('Negative number!')
        is_valid = False
        break
