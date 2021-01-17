people = int(input())

basket_price = 1.50
wreath_price = 3.80
chocolate_bunny_price = 7
total_price = 0

for visitor in range(1, people + 1):
    command = input()
    counter = 0
    sum_price = 0

    while command != 'Finish':

        if command == 'basket':
            sum_price += basket_price
            counter += 1
        elif command == 'wreath':
            sum_price += wreath_price
            counter += 1
        elif command == 'chocolate bunny':
            sum_price += chocolate_bunny_price
            counter += 1
        command = input()

    if counter % 2 == 0:
        sum_price = sum_price * 0.8
    print(f'You purchased {counter} items for {sum_price:.2f} leva.')
    total_price += sum_price

average = total_price / people
print(f'Average bill per client is: {average:.2f} leva.')

