movies = int(input())

max_rating = -99999999999999999999999
min_rating = 99999999999999999999
max_title = ''
min_title = ''

total_rating = 0
for movie in range(1, movies + 1):
    title = input()
    rating = float(input())
    total_rating += rating

    if rating > max_rating:
        max_rating = rating
        max_title = title

    if rating < min_rating:
        min_rating = rating
        min_title = title

print(f'{max_title} is with highest rating: {max_rating:.1f}')
print(f'{min_title} is with lowest rating: {min_rating:.1f}')
print(f'Average rating: {total_rating / movies:.1f}')
