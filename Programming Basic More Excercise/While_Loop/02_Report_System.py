needed_money = int(input())

command = input()

cc_paid = 0
cc_trans = 0
cs_paid = 0
cs_trans = 0
paid_count = 0
total = 0

while command != 'End':
    paid_count += 1
    money = int(command)
    if paid_count % 2 != 0:
        if money > 100:
            print("Error in transaction!")
        else:
            cs_paid += money
            cs_trans += 1
            total += money
            print("Product sold!")
    else:
        if money < 10:
            print("Error in transaction!")
        else:
            cc_paid += money
            cc_trans += 1
            total += money
            print("Product sold!")
    if total >= needed_money:
        break
    else:
        command = input()

if total >= needed_money:
    print(f"Average CS: {cs_paid / cs_trans:.2f}")
    print(f"Average CC: {cc_paid / cc_trans:.2f}")
else:
    print("Failed to collect required money for charity.")

