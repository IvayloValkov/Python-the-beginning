n = int(input())
counter1 = 0
counter2 = 0
counter3 = 0
counter4 = 0
total_grades = 0
total_counter = 0
average = 0
for student in range(1, n + 1):
    grade = float(input())

    if 2.00 <= grade <= 2.99:
        counter1 += 1
    elif 3.00 <= grade <= 3.99:
        counter2 += 1
    elif 4.00 <= grade <= 4.99:
        counter3 += 1
    elif grade >= 5.00:
        counter4 += 1
    total_grades += grade
    total_counter = counter1 + counter2 + counter3 + counter4
    average = total_grades / n

print(f'Top students: {counter4 / total_counter * 100:.2f}%')
print(f'Between 4.00 and 4.99: {counter3 / total_counter * 100:.2f}%')
print(f'Between 3.00 and 3.99: {counter2 / total_counter * 100:.2f}%')
print(f'Fail: {counter1 / total_counter * 100:.2f}%')
print(f'Average: {average:.2f}')


