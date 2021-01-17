import math

days = int(input())
available_food = int(input())
dog_food = float(input())
cat_food = float(input())
turtle_food = float(input())

total_dog = days * dog_food
total_cat = days * cat_food
total_turtle = days * turtle_food / 1000

total_food_needed = total_dog + total_cat + total_turtle

diff = abs(total_food_needed - available_food)

if available_food >= total_food_needed:
    print(f'{math.floor(diff)} kilos of food left.')
else:
    print(f'{math.ceil(diff)} more kilos of food are needed.')
