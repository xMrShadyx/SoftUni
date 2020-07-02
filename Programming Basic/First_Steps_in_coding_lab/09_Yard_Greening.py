cubic_meters = float(input())

price = cubic_meters * 7.61
discount = 0.18 * price
total = price - discount


print(f'The final price is: {total:.2f} lv.')
print(f'The discount is: {discount:.2f} lv.')