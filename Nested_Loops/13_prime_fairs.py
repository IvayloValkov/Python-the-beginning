start1 = int(input())
start2 = int(input())
end1 = int(input())
end2 = int(input())
is_prime = False
counter = 0
for number1 in range(start1, start1 + end1 + 1):
    if number1 % 2 != 0 and number1 % 3 != 0 and number1 % 5 != 0 and number1 % 7 != 0:
        for number2 in range(start2, start2 + end2 + 1):
            if number2 % 2 != 0 and number2 % 3 != 0 and number2 % 5 != 0 and number2 % 7 != 0:
                print(f'{number1}{number2}')