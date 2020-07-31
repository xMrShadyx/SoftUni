amount_students = int(input())

student = 0
b2_b3 = 0
b3_b4 = 0
b4_b5 = 0
ov5 = 0
fail = 0
avr_grade = 0
for i in range(amount_students):
    students_grades = float(input())
    student += 1
    avr_grade += students_grades
    if students_grades <= 2.99:
        b2_b3 += 1
        fail += 1
    elif 3 <= students_grades <= 3.99:
        b3_b4 += 1
    elif 4 <= students_grades <= 4.99:
        b4_b5 += 1
    elif students_grades >= 5:
        ov5 += 1

fails = fail / student * 100
avr_b3b4 = b3_b4 / student * 100
avr_b4b5 = b4_b5 / student * 100
avr_ov5 = ov5 / student * 100
avrt_grade = avr_grade / student

print(f'Top students: {avr_ov5:.2f}%')
print(f'Between 4.00 and 4.99: {avr_b4b5:.2f}%')
print(f'Between 3.00 and 3.99: {avr_b3b4:.2f}%')
print(f'Fail: {fails:.2f}%')
print(f'Average: {avrt_grade:.2f}')