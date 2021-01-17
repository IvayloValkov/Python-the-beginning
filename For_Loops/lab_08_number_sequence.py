n = int(input())

min_number = 9999999999999999999999999999999999999
max_number = -9999999999999999999999999999999999999

for i in range(n):
    current_number = int(input())
    if current_number < min_number:
        min_number = current_number
    if current_number > max_number:
        max_number = current_number

print(f'Max number: {max_number}')
print(f'Min number: {min_number}')
