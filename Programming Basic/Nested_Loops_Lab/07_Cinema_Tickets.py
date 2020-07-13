line = input()
student_tickets = 0
standard_tickets = 0
kid_tickets = 0
total_tickets = 0

while line != 'Finish':
    available_seats = int(input())
    movie_tickets_sold = 0

    ticket_type = input()
    while ticket_type != 'End':
        movie_tickets_sold += 1
        total_tickets += 1
        if ticket_type == 'students':
            student_tickets += 1
        elif ticket_type == 'standard':
            standard_tickets += 1
        else:
            kid_tickets += 1

        if movie_tickets_sold == available_seats:
            break
        ticket_type = input()

    percent = movie_tickets_sold / available_seats * 100
    print(f'{line} - {percent:.2f}% full.')
    line = input()

print(f"Total tickets: {total_tickets}")

percent_student = student_tickets / total_tickets * 100
print(f"{percent_student:.2f}% student tickets.")

percent_standard = standard_tickets / total_tickets * 100
print(f"{percent_standard:.2f}% standard tickets.")

percent_kids = kid_tickets / total_tickets * 100
print(f"{percent_kids:.2f}% kids tickets.")
