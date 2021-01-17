n = int(input())

even_sum = 0
odd_sum = 0

for i in range(n):
    if i % 2 == 0:
        current_number = int(input())
        even_sum += current_number
    elif i % 2 == 1:
        current_number = int(input())
        odd_sum += current_number

if even_sum == odd_sum:
    print('Yes')
    print(f'Sum = {even_sum}')
else:
    print('No')
    print((f'Diff = {abs(even_sum - odd_sum)}'))