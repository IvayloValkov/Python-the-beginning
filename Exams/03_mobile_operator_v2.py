contract_year = input()
contract_type = input()
mobile_internet = input()
months = int(input())

price = 0
if contract_year == 'one':
    if contract_type == 'Small':
        price = 9.98
    elif contract_type == 'Middle':
        price = 18.99
    elif contract_type == 'Large':
        price = 25.98
    elif contract_type == 'ExtraLarge':
        price = 35.99
elif contract_year == 'two':
    if contract_type == 'Small':
        price = 8.58
    elif contract_type == 'Middle':
        price = 17.09
    elif contract_type == 'Large':
        price = 23.59
    elif contract_type == 'ExtraLarge':
        price = 31.79

if mobile_internet == 'yes':
    if price <= 10:
        price += 5.5
    elif price <= 30:
        price += 4.35
    elif price > 30:
        price += 3.85

if contract_year == 'two':
    price -= price * 0.0375

print(f'{price * months:.2f} lv.')