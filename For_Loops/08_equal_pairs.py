pairs = int(input())

previous_pair = 0
current_pair = 0
difference = 0
max_difference = 0

for pair in range(1, pairs + 1):
    number1 = int(input())
    number2 = int(input())
    current_pair = number1 + number2

    if pair > 1:
        difference = abs(previous_pair - current_pair)
        if difference > max_difference:
            max_difference = difference
    previous_pair = current_pair
    current_pair = 0

if max_difference == 0:
    print(f'Yes, value={previous_pair}')
else:
    print(f'No, maxdiff={max_difference}')