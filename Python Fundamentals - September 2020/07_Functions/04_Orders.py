def orders(what, amount):
    if what == 'coffee':
        return f"{1.50 * amount:.2f}"
    elif what == 'coke':
        return f"{1.40 * amount:.2f}"
    elif what == 'water':
        return f"{1 * amount:.2f}"
    elif what == 'snacks':
        return f"{2 * amount:.2f}"


inp1 = input()
inp2 = int(input())

n = orders(inp1, inp2)
print(n)