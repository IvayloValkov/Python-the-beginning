actor = input()
start_points = float(input())

ocenyavashti = int(input())
total_points = 0 + start_points

for ocenka in range(1, ocenyavashti + 1):
    name = input()
    points = float(input())
    points_per_name = len(name) * points / 2
    total_points += points_per_name

    if total_points > 1250.5:

        break
if total_points > 1250.5:
    print(f'Congratulations, {actor} got a nominee for leading role with {total_points:.1f}!')
else:
    print(f'Sorry, {actor} you need {1250.5 - total_points:.1f} more!')


