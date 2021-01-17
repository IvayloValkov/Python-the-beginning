import sys
n = int(input())

max_num = -sys.maxsize
sum_numbers = 0

for i in range(1, n + 1):
    num = int(input())
    sum_numbers += num
    if num > max_num:
        max_num = num

other_sum = sum_numbers - max_num

if other_sum == max_num:
    print('Yes')
    print(f'Sum = {max_num}')
else:
    print('No')
    print(f'Diff = {abs(max_num - other_sum)}')
