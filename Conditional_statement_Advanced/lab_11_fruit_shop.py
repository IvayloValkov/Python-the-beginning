fruit = input()
week_day = input()
quantity = float(input())

if week_day == 'Saturday' or week_day == "Sunday":
    if fruit == 'banana':
        price = 2.70
        total = price * quantity
        print(f'{total:.2f}')
    elif fruit == 'apple':
        price = 1.25
        total = price * quantity
        print(f'{total:.2f}')
    elif fruit == 'orange':
        price = 0.90
        total = price * quantity
        print(f'{total:.2f}')
    elif fruit == 'grapefruit':
        price = 1.60
        total = price * quantity
        print(f'{total:.2f}')
    elif fruit == 'kiwi':
        price = 3.00
        total = price * quantity
        print(f'{total:.2f}')
    elif fruit == 'pineapple':
        price = 5.60
        total = price * quantity
        print(f'{total:.2f}')
    elif fruit == 'grapes':
        price = 4.20
        total = price * quantity
        print(f'{total:.2f}')
    else:
        print('error')
elif week_day == 'Monday' or week_day == 'Tuesday' or week_day == 'Wednesday' or week_day == 'Thursday' or week_day == 'Friday':
    if fruit == 'banana':
        price = 2.50
        total = price * quantity
        print(f'{total:.2f}')
    elif fruit == 'apple':
        price = 1.20
        total = price * quantity
        print(f'{total:.2f}')
    elif fruit == 'orange':
        price = 0.85
        total = price * quantity
        print(f'{total:.2f}')
    elif fruit == 'grapefruit':
        price = 1.45
        total = price * quantity
        print(f'{total:.2f}')
    elif fruit == 'kiwi':
        price = 2.70
        total = price * quantity
        print(f'{total:.2f}')
    elif fruit == 'pineapple':
        price = 5.50
        total = price * quantity
        print(f'{total:.2f}')
    elif fruit == 'grapes':
        price = 3.85
        total = price * quantity
        print(f'{total:.2f}')
    else:
        print('error')
else:
    print('error')

