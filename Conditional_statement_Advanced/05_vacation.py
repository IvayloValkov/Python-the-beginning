budget = float(input())
season = input()

accommodation = ''
location = ''

if budget <= 1000:
    accommodation = 'Camp'
    if season == 'Summer':
        location = 'Alaska'
        budget = budget * 0.65
    elif season == 'Winter':
        location = 'Morocco'
        budget = budget * 0.45

elif 1000 < budget <= 3000:
    accommodation = 'Hut'
    if season == 'Summer':
        location = 'Alaska'
        budget = budget * 0.80
    else:
        location = 'Morocco'
        budget = budget * 0.60
else:
    accommodation = 'Hotel'
    budget = budget * 0.90
    if season == 'Summer':
        location = 'Alaska'
    else:
        location = 'Morocco'

print(f'{location} - {accommodation} - {budget:.2f}')