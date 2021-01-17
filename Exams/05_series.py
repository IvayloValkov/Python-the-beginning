budget = float(input())

n = int(input())
total_price = 0
for serial in range(1, n + 1):
    title = input()
    price = float(input())

    if title == 'Thrones':
        price = price * 0.5
    elif title == 'Lucifer':
        price = price * 0.6
    elif title == 'Protector':
        price = price * 0.7
    elif title == 'TotalDrama':
        price = price * 0.8
    elif title == 'Area':
        price = price * 0.9
    total_price += price

diff = abs(budget - total_price)
if total_price <= budget:
    print(f'You bought all the series and left with {diff:.2f} lv.')
else:
    print(f'You need {diff:.2f} lv. more to buy the series!')
