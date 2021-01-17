movie = input()

total_students_tickets = 0
total_standard_tickets = 0
total_kid_tickets = 0


while movie != 'Finish':
    hall_capacity = int(input())
    ticket_type = input()
    number_tickets = 0
    while ticket_type != 'End':
        number_tickets += 1
        if ticket_type == 'student':
            total_students_tickets += 1
        elif ticket_type == 'standard':
            total_standard_tickets += 1
        elif ticket_type == 'kid':
            total_kid_tickets += 1

        if number_tickets == hall_capacity:
            break

        ticket_type = input()

    print(f'{movie} - {(number_tickets / hall_capacity) * 100:.2f}% full.')

    movie = input()
all_tickets = total_students_tickets + total_standard_tickets + total_kid_tickets
print(f'Total tickets: {all_tickets}')
print(f'{(total_students_tickets / all_tickets) * 100:.2f}% student tickets.')
print(f'{(total_standard_tickets / all_tickets) * 100:.2f}% standard tickets.')
print(f'{(total_kid_tickets / all_tickets) * 100:.2f}% kids tickets.')



