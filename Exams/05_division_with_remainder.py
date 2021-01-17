n = int(input())
counter_p1 = 0
counter_p2 = 0
counter_p3 = 0

for i in range(1, n + 1):
    number = int(input())

    if number % 2 == 0:
        counter_p1 += 1
    if number % 3 == 0:
        counter_p2 += 1
    if number % 4 == 0:
        counter_p3 += 1

print(f'{counter_p1 / n * 100:.2f}%')
print(f'{counter_p2 / n * 100:.2f}%')
print(f'{counter_p3 / n * 100:.2f}%')