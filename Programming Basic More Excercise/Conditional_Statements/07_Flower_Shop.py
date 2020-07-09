#     • Магнолии – 3.25 лева
#     • Зюмбюли – 4 лева
#     • Рози – 3.50 лева
#     • Кактуси – 8 лева
import math

amount_magnolii = int(input())
amount_zyumbyuli = int(input())
amount_roses = int(input())
amount_cactuses = int(input())
gift_amount = float(input())

magnolii = amount_magnolii * 3.25
zyumbyuli = amount_zyumbyuli * 4
roses = amount_roses * 3.50
cactuses = amount_cactuses * 8

total_amount = (magnolii + zyumbyuli + roses + cactuses) * 0.95
# diff = gift_amount - total_amount
# print(diff)

if gift_amount > total_amount:
    diff = math.ceil(gift_amount - total_amount)
    print(f"She will have to borrow {diff} leva.")
else:
    diff = math.floor(total_amount - gift_amount)
    print(f"She is left with {diff} leva.")

