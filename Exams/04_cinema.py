hall_capacity = int(input())
total_income = 0
line = input()
while True:
    if line == 'Movie time!':
        print(f'There are {hall_capacity} seats left in the cinema.')
        break

    people = int(line)

    if hall_capacity < people:
        print(f'The cinema is full.')
        break

    if people % 3 == 0:
        total_income += people * 5 - 5
    else:
        total_income += people * 5

    hall_capacity -= people

    line = input()
print(f'Cinema income - {total_income} lv.')