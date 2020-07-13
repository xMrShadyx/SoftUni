line = input()
prime_sum = 0
not_prime_sum = 0

while line != 'stop':
    number = int(line)

    if number < 0:
        print("Number is negative.")
    else:
        is_prime = False
        counter = 0

        for i in range(1, number + 1):

            if number % i == 0:
                counter += 1

        if counter == 2 or number == 1:
            prime_sum += number
        else:
            not_prime_sum += number

    line = input()
print(f"Sum of all prime numbers is: {prime_sum}")
print(f"Sum of all non prime numbers is: {not_prime_sum}")
