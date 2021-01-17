football_team = input()
games = int(input())
points = 0
total_points = 0
counter_wins = 0
counter_draws = 0
counter_loses = 0
counter_games = 0

if games == 0:
    print(f'{football_team} hasn\'t played any games during this season.')
else:
    for game in range(1, games + 1):
        result = input()
        if result == 'W':
            points = 3
            total_points += points
            counter_wins += 1
            counter_games += 1
        elif result == 'D':
            points = 1
            total_points += points
            counter_draws += 1
            counter_games += 1
        elif result == 'L':
            points = 0
            total_points += points
            counter_loses += 1
            counter_games += 1

    print(f'{football_team} has won {total_points} points during this season.')
    print(f'Total stats:')
    print(f'## W: {counter_wins}')
    print(f'## D: {counter_draws}')
    print(f'## L: {counter_loses}')
    print(f'Win rate: {counter_wins / counter_games * 100:.2f}%')

