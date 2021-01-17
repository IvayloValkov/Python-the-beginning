budget = float(input())
liter_gas = float(input())
day = input()

price_gas = 2.1
price_guide = 100
total_gas = liter_gas * price_gas
total_money = total_gas + price_guide

if day == 'Saturday':
    total_money = total_money - total_money * 0.1
else:
    total_money = total_money - total_money * 0.2

money_left = abs(budget - total_money)
if budget >= total_money:
    print(f'Safari time! Money left: {money_left:.2f} lv.')
else:
    print(f'Not enough money! Money needed: {money_left:.2f} lv.')