budget = float(input())
count_nights = int(input())
price_night = float(input())
additional_expenses_percent = int(input())

if count_nights > 7:
    price_night = price_night * 0.95

total_spent = count_nights * price_night
additional_expenses = budget * additional_expenses_percent / 100
total = total_spent + additional_expenses

diff = abs(total - budget)
if total <= budget:
    print(f'Ivanovi will be left with {diff:.2f} leva after vacation.')
else:
    print(f'{diff:.2f} leva needed.')
