skumria = float(input())
caca = float(input())
palamud = float(input())
safrid = float(input())
midi = int(input())

price_palamud = skumria + skumria * 0.60
price_for_palamud = palamud * price_palamud

price_safrid = caca + caca * 0.80
price_for_safrid = safrid * price_safrid

price_midi = midi * 7.5

total = price_for_palamud + price_for_safrid + price_midi

print(f"{total:.2f}")