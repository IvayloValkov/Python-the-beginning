degrees = int(input())
day_time = input()

if day_time == 'Morning':
    if 10 <= degrees <= 18:
        Outfit = 'Sweatshirt'
        Shoes = 'Sneakers'
        print(f'It\'s {degrees} degrees, get your {Outfit} and {Shoes}.')
    elif 18 < degrees <= 24:
        Outfit = 'Shirt'
        Shoes = 'Moccasins'
        print(f'It\'s {degrees} degrees, get your {Outfit} and {Shoes}.')
    else:
        Outfit = 'T-Shirt'
        Shoes = 'Sandals'
        print(f'It\'s {degrees} degrees, get your {Outfit} and {Shoes}.')

elif day_time == 'Afternoon':
    if 10 <= degrees <= 18:
        Outfit = 'Shirt'
        Shoes = 'Moccasins'
        print(f'It\'s {degrees} degrees, get your {Outfit} and {Shoes}.')
    elif 18 < degrees <= 24:
        Outfit = 'T-Shirt'
        Shoes = 'Sandals'
        print(f'It\'s {degrees} degrees, get your {Outfit} and {Shoes}.')
    else:
        Outfit = 'Swim Suit'
        Shoes = 'Barefoot'
        print(f'It\'s {degrees} degrees, get your {Outfit} and {Shoes}.')

else:
    Outfit = 'Shirt'
    Shoes = 'Moccasins'
    print(f'It\'s {degrees} degrees, get your {Outfit} and {Shoes}.')
