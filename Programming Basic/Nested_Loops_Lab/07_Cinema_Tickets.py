line = input()
standard_ticket = 0
student_ticket = 0
kid_ticket = 0
total_sold_tickets = 0
while line != "Finish":
    free_sits = int(input())
    full_sits = 0
    while full_sits < free_sits:
        type_ticket = input()
        if type_ticket == 'standard':
            standard_ticket += 1
        elif type_ticket == 'student':
            student_ticket += 1
        elif type_ticket == 'kid':
            kid_ticket += 1
        if type_ticket == 'End':
            break
        full_sits += 1
        total_sold_tickets += 1
    print(f'{line} - {full_sits / free_sits * 100:.2f}% full.')
    line = input()
print(f'Total tickets: {total_sold_tickets}')
print(f'{student_ticket / total_sold_tickets * 100:.2f}% student tickets.')
print(f'{standard_ticket / total_sold_tickets * 100:.2f}% standard tickets.')
print(f'{kid_ticket / total_sold_tickets * 100:.2f}% kids tickets.')