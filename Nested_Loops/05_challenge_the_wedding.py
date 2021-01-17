men = int(input())
women = int(input())
tables = int(input())
counter = 0

for man in range(1, men + 1):
    for woman in range(1, women + 1):
        counter += 1
        if counter <= tables:
            print(f'({man} <-> {woman})', end=' ')
