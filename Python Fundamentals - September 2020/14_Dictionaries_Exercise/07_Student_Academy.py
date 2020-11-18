num_rows = int(input())

students = {}

for i in range(1, num_rows + 1):
    student = input()
    grade = float(input())

    if student in students:
        students[student].append(grade)
    students[student] = [grade]

for student, average_grade in students.items():
    students[student] = sum(average_grade) / len(average_grade)

students = dict(sorted(students.items(), key=lambda s: s[1], reverse=True))

for student, average_grade in students.items():
    if average_grade >= 4.5:
        print(f'{student} -> {average_grade:.2f}')
