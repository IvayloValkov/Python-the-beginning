fuel_type = input()
fuel_quantity = float(input())
card = input()

price_gasoline = 2.22
price_diesel = 2.33
price_gas = 0.93

if card == 'Yes' and fuel_type == 'Gasoline':
    price_gasoline = 2.04
elif card == 'Yes' and fuel_type == 'Diesel':
    price_diesel = 2.21
elif card == 'Yes' and fuel_type == 'Gas':
    price_gas = 0.85

total_gasoline = price_gasoline * fuel_quantity
total_diesel = price_diesel * fuel_quantity
total_gas = price_gas * fuel_quantity

if 20 <= fuel_quantity <= 25:
    total_gasoline = total_gasoline * 0.92
    total_diesel = total_diesel * 0.92
    total_gas = total_gas * 0.92
elif fuel_quantity > 25:
    total_gasoline = total_gasoline * 0.90
    total_diesel = total_diesel * 0.90
    total_gas = total_gas * 0.90

if fuel_type == 'Gasoline':
    print(f'{total_gasoline:.2f} lv.')
elif fuel_type == 'Diesel':
    print(f'{total_diesel:.2f} lv.')
else:
    print(f'{total_gas:.2f} lv.')