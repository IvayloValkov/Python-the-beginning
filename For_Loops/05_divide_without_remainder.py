n = int(input())

group1_count = 0
group2_count = 0
group3_count = 0

for i in range(1, n + 1):
    number = int(input())
    if number % 2 == 0:
        group1_count += 1
    if number % 3 == 0:
        group2_count += 1
    if number % 4 == 0:
        group3_count += 1


print(f'{group1_count/n*100:.2f}%')
print(f'{group2_count/n*100:.2f}%')
print(f'{group3_count/n*100:.2f}%')

