count_bad_grades = int(input())
current_count_bad_grades = 0

total_grades = 0
count_grades = 0

line = input()
while line != "Enough":
    task_name = line
    grade = int(input())
    count_grades += 1
    total_grades += grade

    if grade <= 4:
        current_count_bad_grades += 1

    if current_count_bad_grades == count_bad_grades:
        print(f'You need a break, {count_bad_grades} poor grades.')
        break

    line = input()

if line == 'Enough':
    average_grades = total_grades / count_grades
    print(f"Average score: {average_grades:.2f}")
    print(f"Number of problems: {count_grades}")
    print(f"Last problem: {task_name}")


    