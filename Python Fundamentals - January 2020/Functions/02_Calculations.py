def multiply(a, b):
    return a * b


def add(a, b):
    return a + b


def divide(a, b):
    return a // b


def subtrack(a, b):
    return a - b


def execute(a, b, operation):
    # Listing
    mapping = [
        ['multiply', multiply],
        ['add', add],
        ['divide', divide],
        ['subtrack', subtrack],
    ]
    for operation_name, fn in mapping:
        if operation_name == operation:
            return fn(a, b)


a = int(input())
b = int(input())
operation = input()
print(execute(a, b, operation))

# Dictionary
# mapping = {
#     'multiply': multiply,
#     'sum': sum,
#     'divide': divide,
#     'subtrack': subtrack,
# }
# fn = mapping[operation]
# return fn(a, b)

# if else statement
# if operation == 'multiply':
#     return multiply(a, b)
# if operation == 'sum':
#     return sum(a, b)
# if operation == 'divide':
#     return divide(a, b)
# if operation == 'subtrack':
#     return subtrack(a, b)
