movie_type = input()
rows = int(input())
columns = int(input())

room = rows * columns

if movie_type == 'Premiere':
    print(f'{room * 12:.2f} leva')
elif movie_type == 'Normal':
    print(f'{room * 7.5:.2f} leva')
elif movie_type == 'Discount':
    print(f'{room * 5:.2f}')