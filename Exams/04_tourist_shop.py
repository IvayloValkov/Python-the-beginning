budget = float(input())

products_counter = 0
total_price = 0
line = input()
command_stop = True

while line != 'Stop':
    price = float(input())
    products_counter += 1

    if products_counter % 3 == 0:
        price = price * 0.5

    if price + total_price > budget:
        command_stop = False
        diff = (total_price + price) - budget
        print(f'You don\'t have enough money!')
        print(f'You need {diff:.2f} leva!')
        break

    total_price += price

    line = input()

if command_stop:
    print(f'You bought {products_counter} products for {total_price:.2f} leva.')



