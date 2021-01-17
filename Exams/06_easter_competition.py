n = int(input())
topchef = ''
maxscore = -9999999

for chef in range(1, n + 1):
    name = input()
    score = input()
    points = 0
    while score != 'Stop':
        points += int(score)

        score = input()
    print(f'{name} has {points} points.')

    if points > maxscore:
        maxscore = points
        topchef = name
        print(f'{topchef} is the new number 1!')



print(f'{topchef} won competition with {maxscore} points!')
