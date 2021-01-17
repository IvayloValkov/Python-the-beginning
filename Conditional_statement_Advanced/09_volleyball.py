import math

year = input()
p = int(input())
h = int(input())

weekends_sofia = 48 - h
games_sofia = weekends_sofia * 0.75
games_not_sofia = h
games_holidays_sofia = p * 2/3

total_games = games_sofia + games_not_sofia + games_holidays_sofia

if year == 'leap':
    total_games += total_games * 0.15

print(f'{math.floor(total_games)}')



