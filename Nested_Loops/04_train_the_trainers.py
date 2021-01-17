judges = int(input())
total_sum = 0
counter = 0

line = input()
while line != 'Finish':
    sum_grades = 0
    for i in range(judges):
        grade = float(input())
        sum_grades += grade
        total_sum += grade
        counter += 1

    print(f'{line} - {sum_grades / judges:.2f}.')
    line = input()

print(f'Student\'s final assessment is {total_sum / counter:.2f}.')