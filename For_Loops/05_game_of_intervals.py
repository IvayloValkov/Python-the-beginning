n = int(input())
counter1 = 0
counter2 = 0
counter3 = 0
counter4 = 0
counter5 = 0
counter6 = 0
total_counter = 0

points = 0
for i in range(1, n + 1):
    number = int(input())

    if 0 <= number <= 9:
        points += number * 0.2
        counter1 += 1
    elif 10 <= number <= 19:
        points += number * 0.3
        counter2 += 1
    elif 20 <= number <= 29:
        points += number * 0.4
        counter3 += 1
    elif 30 <= number <= 39:
        points += 50
        counter4 += 1
    elif 40 <= number <= 50:
        points += 100
        counter5 += 1
    elif number > 50 or number < 0:
        points = points / 2
        counter6 += 1
    total_counter = counter1 + counter2 + counter3 + counter4 + counter5 + counter6

print(f'{points:.2f}')
print(f'From 0 to 9: {counter1 / total_counter * 100:.2f}%')
print(f'From 10 to 19: {counter2 / total_counter * 100:.2f}%')
print(f'From 20 to 29: {counter3 / total_counter * 100:.2f}%')
print(f'From 30 to 39: {counter4 / total_counter * 100:.2f}%')
print(f'From 40 to 50: {counter5 / total_counter * 100:.2f}%')
print(f'Invalid numbers: {counter6 / total_counter * 100:.2f}%')
