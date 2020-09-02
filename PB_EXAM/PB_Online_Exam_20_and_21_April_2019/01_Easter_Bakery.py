amount_cozunacs = int(input())
amount_eggs = int(input())
amount_cookies = int(input())

price_cozunacs = amount_cozunacs * 3.2
price_eggs = amount_eggs * 4.35
price_cookies = amount_cookies * 5.40
price_single_egg = amount_eggs * 12 * 0.15
total = price_cozunacs + price_eggs + price_cookies + price_single_egg

print(f"{total:.2f}")