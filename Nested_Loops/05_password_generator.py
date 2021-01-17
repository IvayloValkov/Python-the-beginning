n = int(input())
l = int(input())

for first_digit in range(1, n + 1):
    for second_digit in range(1, n + 1):
        for third_digit in range(ord("a"), (l + 97)):
            for fourth_digit in range(ord("a"), (l + 97)):
                for fifth_digit in range((max(first_digit, second_digit) + 1), n + 1):
                    print(f'{first_digit}{second_digit}{chr(third_digit)}{chr(fourth_digit)}{fifth_digit}', end=' ')