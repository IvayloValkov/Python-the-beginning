needed_money = int(input())

transaction_counter = 0
counter_cash = 0
counter_card = 0
total_cash = 0
total_card = 0

while True:
    transaction = input()
    if transaction == 'End':
        print(f'Failed to collect required money for charity.')
        break
    transaction_counter += 1
    if transaction_counter % 2 != 0:
        product_cash = int(transaction)
        if product_cash <= 100:
            print(f'Product sold!')
            counter_cash += 1
            total_cash += product_cash
        else:
            print(f'Error in transaction!')
    else:
        product_card = int(transaction)
        if product_card >= 10:
            print(f'Product sold!')
            counter_card += 1
            total_card += product_card
        else:
            print(f'Error in transaction!')

    if total_cash + total_card >= needed_money:
        print(f'Average CS: {total_cash / counter_cash:.2f}')
        print(f'Average CC: {total_card / counter_card:.2f}')
        break
