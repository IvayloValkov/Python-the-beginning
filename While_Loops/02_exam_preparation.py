bad_grades = int(input())

average_score = 0
grade_sum = 0
grade_counter = 0
bad_grades_counter = 0
last_task = ''

while True:
    task = input()

    if task == 'Enough':
        print(f'Average score: {grade_sum / grade_counter:.2f}')
        print(f'Number of problems: {grade_counter}')
        print(f'Last problem: {last_task}')
        break

    last_task = task
    grade = int(input())
    grade_counter += 1
    grade_sum += grade

    if grade <= 4:
        bad_grades_counter += 1

    if bad_grades_counter == bad_grades:
        print(f'You need a break, {bad_grades} poor grades.')
        break