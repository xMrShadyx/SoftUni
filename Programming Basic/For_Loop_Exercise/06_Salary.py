n = int(input())

salary = int(input())

for i in range(0, n):
    tab = input()

    if tab == 'Facebook':
        salary -= 150
    elif tab == 'Instagram':
        salary -= 100
    elif tab == 'Reddit':
        salary -= 50

    if salary <= 0:
        break

if salary > 0:
    print(salary)
else:
    print('You have lost your salary.')
