inherited_money = float(input())
n = int(input())
starting_years = 18
spent_money = 0

for year in range(1800, n + 1):
    if year % 2 == 0:
        spent_money += 12000
    else:
        spent_money += 12000 + 50 * starting_years
    starting_years += 1

diff = abs(inherited_money - spent_money)
if inherited_money >= spent_money:
    print(f'Yes! He will live a carefree life and will have {diff:.2f} dollars left.')
else:
    print(f'He will need {diff:.2f} dollars to survive.')
