budget = float(input())
category = input()
number_people = int(input())

ticket_price = 0
transport = 0
if category == 'VIP':
    ticket_price = 499.99
    if 1 <= number_people <= 4:
        transport = budget * 0.75
    elif 5 <= number_people <= 9:
        transport = budget * 0.6
    elif 10 <= number_people <= 24:
        transport = budget * 0.5
    elif 25 <= number_people <= 49:
        transport = budget * 0.4
    elif number_people >= 50:
        transport = budget * 0.25
elif category == 'Normal':
    ticket_price = 249.99
    if 1 <= number_people <= 4:
        transport = budget * 0.75
    elif 5 <= number_people <= 9:
        transport = budget * 0.6
    elif 10 <= number_people <= 24:
        transport = budget * 0.5
    elif 25 <= number_people <= 49:
        transport = budget * 0.4
    elif number_people >= 50:
        transport = budget * 0.25

budget_left = budget - transport
all_tickets = ticket_price * number_people
diff = abs(budget_left - all_tickets)
if all_tickets <= budget_left:
    print(f'Yes! You have {diff:.2f} leva left.')
else:
    print(f'Not enough money! You need {diff:.2f} leva.')