# Made by Vladislav Vasilev

def length(password):
    if len(password) < 6 or len(password) > 10:
        return "Password must be between 6 and 10 characters"


def only_letters_and_digits(password):
    for char in password:
        if not char.isalpha() and not char.isdigit():
            return "Password must consist only of letters and digits"


def two_digits(password):
    digit_c = 0
    for char in password:
        if char.isdigit():
            digit_c += 1

    if digit_c < 2:
        return "Password must have at least 2 digits"


def validate(password):
    validators = [
        length,
        only_letters_and_digits,
        two_digits
    ]

    validate_errors = []

    for validator in validators:
        res = validator(password)

        if res is not None:
            validate_errors.append(res)

    if len(validate_errors) == 0:
        return "Password is valid"
    else:
        return "\n".join(validate_errors)


password = input()

print(validate(password))
