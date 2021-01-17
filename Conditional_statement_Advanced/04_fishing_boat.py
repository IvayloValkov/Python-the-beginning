budget = int(input())
season = input()
fishermen = int(input())

rent = 0

if season == 'Spring':
    rent = 3000
elif season == 'Summer' or season == 'Autumn':
    rent = 4200
else:
    rent = 2600

if fishermen <= 6:
    rent -= rent * 0.1
elif 7 <= fishermen <= 11:
    rent -= rent * 0.15
else:
    rent -= rent * 0.25

if fishermen % 2 == 0 and season != 'Autumn':
    rent -= rent * 0.05

result = abs(budget - rent)
if budget >= rent:
    print(f'Yes! You have {result:.2f} leva left.')
else:
    print(f'Not enough money! You need {result:.2f} leva.')