fuel = input()
liter_in_tank = float(input())

if fuel == 'Diesel':
    if liter_in_tank >= 25:
        print(f'You have enough {fuel.casefold()}.')
    elif liter_in_tank < 25:
        print(f'Fill your tank with {fuel.casefold()}!')
elif fuel == 'Gasoline':
    if liter_in_tank >= 25:
        print(f'You have enough {fuel.casefold()}.')
    elif liter_in_tank < 25:
        print(f'Fill your tank with {fuel.casefold()}!')
elif fuel == 'Gas':
    if liter_in_tank >= 25:
        print(f'You have enough {fuel.casefold()}.')
    elif liter_in_tank < 25:
        print(f'Fill your tank with {fuel.casefold()}!')
else:
    print(f'Invalid fuel!')