needed_money = float(input())
owned_money = float(input())


spend_count = 0
days = 0
while True:
    action = input()
    current_money = float(input())
    days += 1

    if action == 'spend':
        if current_money > owned_money:
            owned_money = current_money
        owned_money -= current_money
        spend_count += 1

        if spend_count == 5:
            print('You can\'t save the money.')
            print(f'{days}')
            break

    else:
        owned_money += current_money
        spend_count = 0
        if owned_money >= needed_money:
            print(f'You saved the money for {days} days.')
            break

