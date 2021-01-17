n = int(input())

group1_count = 0
group2_count = 0
group3_count = 0
group4_count = 0
group5_count = 0

for i in range(1, n + 1):
    number = int(input())
    if number < 200:
        group1_count += 1
    elif 200 <= number <= 399:
        group2_count += 1
    elif 400 <= number <= 599:
        group3_count += 1
    elif 600 <= number <= 799:
        group4_count += 1
    elif number >= 800:
        group5_count += 1

print(f'{group1_count/n*100:.2f}%')
print(f'{group2_count/n*100:.2f}%')
print(f'{group3_count/n*100:.2f}%')
print(f'{group4_count/n*100:.2f}%')
print(f'{group5_count/n*100:.2f}%')