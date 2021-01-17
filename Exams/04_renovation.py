import math

height = int(input())
width = int(input())
windows = int(input())
overall_area = height * width * 4
area = overall_area - (overall_area * windows / 100)
total_paint_used = 0

line = input()
while True:
    if line == 'Tired!':
        print(f'{math.ceil(area)} quadratic m left.')
        break
    paint_used = int(line)
    total_paint_used += paint_used
    area -= paint_used
    if area < 0:
        print(f'All walls are painted and you have {abs(math.ceil(area))} l paint left!')
        break
    if area == 0:
        print(f'All walls are painted! Great job, Pesho!')
        break
    line = input()