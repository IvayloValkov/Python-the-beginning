bottles = int(input())
total_ml = bottles * 750

counter = 0
washed_dishes = 0
washed_pots = 0
line = input()
while True:
    if line == 'End':
        print(f'Detergent was enough!')
        print(f'{washed_dishes} dishes and {washed_pots} pots were washed.')
        print(f'Leftover detergent {abs(total_ml)} ml.')
        break
    counter += 1
    if counter % 3 != 0:
        dishes = int(line)
        washed_dishes += dishes
        total_ml -= 5 * dishes
    elif counter % 3 == 0:
        pots = int(line)
        washed_pots += pots
        total_ml -= 15 * pots
    if total_ml < 0:
        print(f'Not enough detergent, {abs(total_ml)} ml. more necessary!')
        break
    line = input()

