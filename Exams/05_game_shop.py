games = int(input())

counter1 = 0
counter2 = 0
counter3 = 0
counter4 = 0
total_counter = 0

for i in range(1, games + 1):
    game_title = input()

    if game_title == 'Hearthstone':
        counter1 += 1
        total_counter += 1
    elif game_title == 'Fornite':
        counter2 += 1
        total_counter += 1
    elif game_title == 'Overwatch':
        counter3 += 1
        total_counter += 1
    else:
        counter4 += 1
        total_counter += 1
print(f'Hearthstone - {counter1 / total_counter * 100:.2f}%')
print(f'Fornite - {counter2 / total_counter * 100:.2f}%')
print(f'Overwatch - {counter3 / total_counter * 100:.2f}%')
print(f'Others - {counter4 / total_counter * 100:.2f}%')

