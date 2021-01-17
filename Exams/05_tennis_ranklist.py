import math

tournaments = int(input())
start_points = int(input())
points = 0
counter_w = 0
for tour in range(1, tournaments + 1):
    stage = input()

    if stage == 'W':
        points += 2000
        counter_w += 1
    elif stage == 'F':
        points += 1200
    elif stage == 'SF':
        points += 720

print(f'Final points: {points + start_points}')
print(f'Average points: {math.floor(points / tournaments)}')
print(f'{counter_w / tournaments * 100:.2f}%')