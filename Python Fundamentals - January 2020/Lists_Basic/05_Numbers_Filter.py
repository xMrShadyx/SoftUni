def is_even(number):
    return number % 2 == 0


def is_odd(number):
    return number % 2 != 0


def is_negative(number):
    return number < 0


def is_positive(number):
    return number >= 0


FILTERS_MAP = {
    'even': is_even,
    'odd': is_odd,
    'positive': is_positive,
    'negative': is_negative,
}

n = int(input())

numbers = [int(input()) for _ in range(n)]
command = input()

filter_fn = FILTERS_MAP[command]
print([n for n in numbers if filter_fn(n)])

#in case to use FILTER_MAP with lambda remove the Functions.
'''
FILTERS_MAP = {
    'even': lambda number: number % 2 == 0,
    'odd': lambda number: number % 2 != 0,
    'positive': lambda number: number >= 0,
    'negative': lambda number: number < 0,
}
#change filter_fn
filter_fn = FILTERS_MAP[input()]
# And remove command = input()
or:
filter_fn = FILTER_MAP.get(input())

if filter_fn is not None:
    print([n for n in numbers if filter_fn(n)])
else:
    print("Unsupported command.")
'''