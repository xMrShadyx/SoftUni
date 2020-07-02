N = int(input())
P1 = int(input())
P2 = int(input())
H = float(input())

p1 = H * P1
p2 = H * P2

total = p1 + p2

volume = (total / N) * 100
pipe1 = p1 / total * 100
pipe2 = p2 / total * 100


if total < N:
    print(f"The pool is {volume:.2f}% full. Pipe 1: {pipe1:.2f}%. Pipe 2: {pipe2:.2f}%.")
else:
    diff = abs(N - total)
    print(f"For {H:.2f} hours the pool overflows with {diff:.2f} liters.")

