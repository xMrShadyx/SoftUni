happiness_indexes = [int(n) for n in input().split(' ')]
improved_factor = int(input())

factored_happiness_indexes = [v * improved_factor for v in happiness_indexes]
average_happiness = sum(factored_happiness_indexes) / len(factored_happiness_indexes)
happy_value = list(filter(lambda n: n >= average_happiness, factored_happiness_indexes))

happy_count = len(happy_value)
total_count = len(happiness_indexes)

if happy_count >= (total_count / 2):
    print(f'Score: {happy_count}/{total_count}. Employees are happy!')
else:
    print(f'Score: {happy_count}/{total_count}. Employees are not happy!')