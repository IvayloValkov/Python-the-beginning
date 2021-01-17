width = int(input())
height = int(input())

cake_pieces = width * height

while cake_pieces > 0:
    line = input()

    if line == 'STOP':
        break

    cake_pieces -= int(line)

if cake_pieces <= 0:
    print(f'No more cake left! You need {abs(cake_pieces)} pieces more.')
else:
    print(f'{cake_pieces} pieces are left.')