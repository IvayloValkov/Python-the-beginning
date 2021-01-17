stadium = int(input())
fans = int(input())
countera = 0
counterb = 0
counterv = 0
counterg = 0
total_counter = 0

for fan in range(1 , fans + 1):
    sector = input()

    if sector == 'A':
        countera += 1
    elif sector == 'B':
        counterb += 1
    elif sector == 'V':
        counterv += 1
    elif sector == 'G':
        counterg += 1
    total_counter = countera + counterb + counterv + counterg

print(f'{countera / total_counter * 100:.2f}%')
print(f'{counterb / total_counter * 100:.2f}%')
print(f'{counterv / total_counter * 100:.2f}%')
print(f'{counterg / total_counter * 100:.2f}%')
print(f'{fans / stadium * 100:.2f}%')
