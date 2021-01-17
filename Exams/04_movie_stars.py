budget = float(input())

name = input()
total_pay = 0
while True:
    if name == 'ACTION':
        print(f'We are left with {budget:.2f} leva.')
        break
    else:
        if len(name) > 15:
            pay = budget * 0.2
            budget -= pay
            total_pay += pay
        else:
            pay = float(input())
            total_pay += pay
            budget -= pay

    if budget < 0:
        print(f'We need {abs(budget):.2f} leva for our actors.')
        break

    name = input()


