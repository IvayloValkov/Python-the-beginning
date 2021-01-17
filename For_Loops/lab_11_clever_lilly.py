age = int(input())
price_washing_machine = float(input())
toy_price = int(input())

saved_money = 0

for i in range(1, age + 1):
    if i % 2 == 0:
        saved_money += (10 * i / 2) - 1
    else:
        saved_money += toy_price

result = abs(saved_money - price_washing_machine)

if saved_money >= price_washing_machine:
    print(f'Yes! {result:.2f}')
else:
    print(f'No! {result:.2f}')


