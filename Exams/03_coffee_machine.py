drink = input()
sugar = input()
number_drinks = int(input())

price = 0

if drink == 'Espresso':
    if sugar == 'Without':
        price = 0.90
        price = price * 0.65
    elif sugar == 'Normal':
        price = 1
    elif sugar == 'Extra':
        price = 1.20
elif drink == 'Cappuccino':
    if sugar == 'Without':
        price = 1
        price = price * 0.65
    elif sugar == 'Normal':
        price = 1.20
    elif sugar == 'Extra':
        price = 1.60
elif drink == 'Tea':
    if sugar == 'Without':
        price = 0.50
        price = price * 0.65
    elif sugar == 'Normal':
        price = 0.60
    elif sugar == 'Extra':
        price = 0.70

total = price * number_drinks

if drink == 'Espresso' and number_drinks >= 5:
    total = total * 0.75

if total > 15:
    total = total * 0.8

print(f'You bought {number_drinks} cups of {drink} for {total:.2f} lv.')
