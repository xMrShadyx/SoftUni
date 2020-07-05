command = input()
sum = 0.0

while command != "NoMoreMoney":
    money = float(command)

    if money < 0:
        print("Invalid operation!")
        break

    print(f"Increase: {money:.2f}")
    sum += money

    command = input()

print(f"Total: {sum:.2f}")

