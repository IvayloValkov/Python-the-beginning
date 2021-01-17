movie = input()
package = input()
tickets = int(input())

price = 0

if movie == 'John Wick':
    if package == 'Drink':
        price = 12
    elif package == 'Popcorn':
        price = 15
    elif package == 'Menu':
        price = 19
elif movie == 'Star Wars':
    if package == 'Drink':
        price = 18
    elif package == 'Popcorn':
        price = 25
    elif package == 'Menu':
        price = 30
    if tickets >= 4:
        price = price * 0.7
elif movie == 'Jumanji':
    if package == 'Drink':
        price = 9
    elif package == 'Popcorn':
        price = 11
    elif package == 'Menu':
        price = 14
    if tickets == 2:
        price = price * 0.85

total = price * tickets
print(f'Your bill is {total:.2f} leva.')