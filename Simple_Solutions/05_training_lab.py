w = float(input())
h = float(input())

lenght_cm = w * 100
width = h * 100
corridor = 100
total_width = width - corridor
place_per_length = lenght_cm // 120
place_per_width = total_width // 70
total_places = place_per_length * place_per_width
door = 1
bench = 2
overall_places = total_places - door - bench
print(f'{int(overall_places)}')
