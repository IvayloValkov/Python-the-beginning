first_number = int(input())
second_number = int(input())

for i in range(first_number, second_number + 1):
    number = i
    even_sum = 0
    odd_sum = 0
    for position in range(1, 7):
        digit = number % 10
        number = number // 10

        if position % 2 == 0:
            even_sum += digit
        else:
            odd_sum += digit

    if even_sum == odd_sum:
        print(f'{i}', end=' ')

