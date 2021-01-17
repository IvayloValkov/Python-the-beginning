number = float(input())

while True:
    if number >= 0:
        print(f'Result: {number * 2:.2f}')
    if number < 0:
        print(f'Negative number!')
        break
    number = float(input())
