x = float(input())
y = float(input())
h = float(input())

front_back_walls = (x * x) * 2
door = 1.2 * 2
side_walls = (x * y) * 2
windows = (1.5 * 1.5) * 2
roof = ((x * h) / 2) * 2 + side_walls
total_house = (front_back_walls - door) + (side_walls - windows)
green_paint = total_house / 3.4
red_paint = roof / 4.3

print(f'{green_paint:.2f}')
print(f'{red_paint:.2f}')