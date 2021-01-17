number_juniors = int(input())
number_seniors = int(input())
trace = input()
budget = 0
if trace == 'trail':
    price_juniors = 5.50
    price_seniors = 7
    budget = price_juniors * number_juniors + price_seniors * number_seniors
elif trace == 'cross-country':
    price_juniors = 8
    price_seniors = 9.50
    budget = price_juniors * number_juniors + price_seniors * number_seniors
    if number_juniors + number_seniors >= 50:
        budget -= budget * 0.25
elif trace == 'downhill':
    price_juniors = 12.25
    price_seniors = 13.75
    budget = price_juniors * number_juniors + price_seniors * number_seniors
elif trace == 'road':
    price_juniors = 20
    price_seniors = 21.50
    budget = price_juniors * number_juniors + price_seniors * number_seniors

budget -= budget * 0.05
print(f'{budget:.2f}')
