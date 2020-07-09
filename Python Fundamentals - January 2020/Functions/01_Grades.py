def is_fail(grade):
    return 2.00 <= grade <= 2.99


def is_poor(grade):
    return 3.00 <= grade <= 3.49


def is_good(grade):
    return 3.50 <= grade <= 4.49


def is_very_good(grade):
    return 4.50 <= grade <= 5.49


def is_excellent(grade):
    return 5.50 <= grade <= 6


def solve(grade):
    grades = [
        [is_fail, 'Fail'],
        [is_poor, 'Poor'],
        [is_good, 'Good'],
        [is_very_good, 'Very Good'],
        [is_excellent, 'Excellent'],
    ]
    for fn, result in grades:
        if fn(grade):
            return result


grade = float(input())
print(f'{solve(grade)}')
