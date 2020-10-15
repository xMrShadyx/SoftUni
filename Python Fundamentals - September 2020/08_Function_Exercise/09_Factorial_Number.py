def calc_factorial(n):
    res = 1
    for num in range(1, n + 1):
        res *= num

    return res


number1 = int(input())
number2 = int(input())

fact_num1 = calc_factorial(number1)
fact_num2 = calc_factorial(number2)

result = fact_num1 / fact_num2
print(f"{result:.2f}")
