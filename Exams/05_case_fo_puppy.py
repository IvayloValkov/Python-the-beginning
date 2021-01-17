food = int(input())
food_in_grams = food * 1000

command = input()

while command != 'Adopted':
    eaten_food = int(command)
    food_in_grams -= eaten_food
    command = input()

if food_in_grams >= 0:
    print(f'Food is enough! Leftovers: {food_in_grams} grams.')
else:
    print(f'Food is not enough. You need {abs(food_in_grams)} grams more.')

