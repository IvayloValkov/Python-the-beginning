first_player = input()
second_player = input()

winner = ''
points1 = 0
points2 = 0
line = input()
while True:
    if line == 'End of game':
        print(f'{first_player} has {points1} points')
        print(f'{second_player} has {points2} points')
        break
    card1 = int(line)
    card2 = int(input())

    if card1 > card2:
        points1 += card1 - card2
    elif card2 > card1:
        points2 += card2 - card1
    elif card1 == card2:
        print(f'Number wars!')
        card1 = int(input())
        card2 = int(input())
        if card1 > card2:
            winner = first_player
            print(f'{winner} is winner with {points1} points')
            break
        elif card1 < card2:
            winner = second_player
            print(f'{winner} is winner with {points2} points')
            break

    line = input()



