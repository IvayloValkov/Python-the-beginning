movie = input()
student_counter = 0
standard_counter = 0
kid_counter = 0

while movie != 'Finish':
    hall_capacity = int(input())
    ticket = input()
    ticket_counter = 0
    while ticket != 'End':
        ticket_counter += 1
        if ticket == 'student':
            student_counter += 1
        elif ticket == 'standard':
            standard_counter += 1
        elif ticket == 'kid':
            kid_counter += 1

        if ticket_counter == hall_capacity:
            break
        ticket = input()

    print(f'{movie} - {(ticket_counter / hall_capacity) * 100:.2f}% full.')

    movie = input()

total_tickets = student_counter + standard_counter + kid_counter
print(f'Total tickets: {total_tickets}')
print(f'{(student_counter / total_tickets) * 100:.2f}% student tickets.')
print(f'{(standard_counter / total_tickets) * 100:.2f}% standard tickets.')
print(f'{(kid_counter / total_tickets) * 100:.2f}% kids tickets.')