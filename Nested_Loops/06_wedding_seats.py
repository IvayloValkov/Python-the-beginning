sectors = input()
rows = int(input())
seats_odd_row = int(input())
counter = 0

for sector in range(65, ord(sectors) + 1):
    for row in range(1, rows + 1):
        if row % 2 != 0:
            for seat in range(ord("a"), (96 + seats_odd_row + 1)):
                print(f'{chr(sector)}{row}{chr(seat)}')
                counter += 1
        if row % 2 == 0:
            for seat in range(ord("a"), (96 + seats_odd_row + 2 + 1)):
                print(f'{chr(sector)}{row}{chr(seat)}')
                counter += 1
    rows += 1

print(f'{counter}')


