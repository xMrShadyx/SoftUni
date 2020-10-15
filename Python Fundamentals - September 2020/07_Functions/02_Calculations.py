def calc(ope, val1, val2):
    if ope == 'multiply':
        return val1 * val2
    elif ope == 'divide':
        return int(val1 / val2)
    elif ope == 'add':
        return val1 + val2
    elif ope == 'subtract':
        return val1 - val2


inp_ope = input()
inp_val1 = int(input())
inp_val2 = int(input())

n = calc(inp_ope, inp_val1, inp_val2)
print(n)
