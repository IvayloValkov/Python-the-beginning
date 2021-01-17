name = input()
sum_grades = 0
average_grade = 0
level = 0

while True:
    annual_grade = float(input())
    if annual_grade < 4:
        grade = float(input())
        if annual_grade < 4:
            level += 1
            print(f'{name} has been excluded at {level} grade')
            break
    else:
        level += 1

    sum_grades += annual_grade
    average_grade = sum_grades / level
    if level == 12:
        print(f'{name} graduated. Average grade: {average_grade:.2f}')
        break






