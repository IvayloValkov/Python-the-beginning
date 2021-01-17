budget = float(input())
season = input()

destination = ''
accommodation = ''
price = 0

if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        accommodation = 'Camp'
        price = budget * 0.3
    else:
        accommodation = 'Hotel'
        price = budget * 0.7

elif budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        accommodation = 'Camp'
        price = budget * 0.4
    else:
        accommodation = 'Hotel'
        price = budget * 0.8
else:
    destination = 'Europe'
    accommodation = 'Hotel'
    price = budget * 0.90

print(f'Somewhere in {destination}')
print(f'{accommodation} - {price:.2f}')