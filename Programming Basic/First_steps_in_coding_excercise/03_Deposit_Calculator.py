deposit = float(input())
deposit_mothns = int(input())
yearly_depsit = float(input())

price = deposit + deposit_mothns * ((deposit * yearly_depsit / 100) / 12)

print(price)