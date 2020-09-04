rent = int(input())

oscars = rent * 0.7
catering = oscars * 0.85
sound = catering / 2

total = oscars + catering + sound + rent

print(f"{total:.2f}")