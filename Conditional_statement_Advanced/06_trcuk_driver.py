season = input()
distance = float(input())

price_per_km = 0

if distance <= 5000:
    if season == 'Spring' or season == 'Autumn':
        price_per_km = 0.75
    elif season == 'Summer':
        price_per_km = 0.90
    else:
        price_per_km = 1.05

elif 5000 < distance <= 10000:
    if season == 'Spring' or season == 'Autumn':
        price_per_km = 0.95
    elif season == 'Summer':
        price_per_km = 1.10
    else:
        price_per_km = 1.25

elif 10000 < distance <= 20000:
    price_per_km = 1.45

total_money = price_per_km * distance * 4
salary = total_money - total_money * 0.1
print(f'{salary:.2f}')