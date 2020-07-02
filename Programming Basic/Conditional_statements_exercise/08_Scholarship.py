import math

income = float(input())
grade = float(input())
min_salary = float(input())

scholarship = min_salary * 0.35
excellent_scholarship = grade * 25

if income < min_salary and grade > 4.50:
      if scholarship > excellent_scholarship:
            print(f'You get a Social scholarship {math.floor(scholarship)} BGN')
      elif grade > 5.50:
            print(f'You get a scholarship for excellent results {math.floor(excellent_scholarship)} BGN')
else:
      print('You cannot get a scholarship!')







# if income < min_salary and grade > 4.5 or grade < 5.5:
#       print(f'You get a Social scholarship {math.floor(stipendia)} BGN')
# elif grade >= 5.5:
#       print(f'You get a scholarship for excellent results {math.floor(excellent_scholarship)} BGN')
# else:
#       print('You cannot get a scholarship!')