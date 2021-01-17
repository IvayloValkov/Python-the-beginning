import sys

n = int(input())

odd_sum = 0
odd_max = -sys.maxsize
odd_min = sys.maxsize
even_sum = 0
even_max = -sys.maxsize
even_min = sys.maxsize


for i in range(1, n + 1):
    input_number = float(input())
    if i % 2 == 0:
        even_sum += input_number
        if input_number > even_max:
            even_max = input_number
        if input_number < even_min:
            even_min = input_number
    else:
        odd_sum += input_number
        if input_number > odd_max:
            odd_max = input_number
        if input_number < odd_min:
            odd_min = input_number

print(f'OddSum={odd_sum:.2f},')
if odd_min != sys.maxsize:
    print(f'OddMin={odd_min:.2f},')
else:
    print(f'OddMin=No,')
if odd_max != -sys.maxsize:
    print(f'OddMax={odd_max:.2f},')
else:
    print(f'OddMax=No,')

print(f'EvenSum={even_sum:.2f},')
if even_min != sys.maxsize:
    print(f'EvenMin={even_min:.2f},')
else:
    print(f'EvenMin=No,')
if even_max != -sys.maxsize:
    print(f'EvenMax={even_max:.2f}')
else:
    print(f'EvenMax=No')

