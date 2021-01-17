hrizantemi_number = int(input())
roses_number = int(input())
tullips_number = int(input())
season = input()
is_holiday = input()
decoration = 2

if season == 'Spring' or season == 'Summer':
    hrizantemi_price = 2.00
    roses_price = 4.10
    tulips_price = 2.50
    whole_bouqet = hrizantemi_number * hrizantemi_price + roses_number * roses_price + tullips_number * tulips_price
    if is_holiday == 'Y':
        whole_bouqet += whole_bouqet * 0.15
        if season == 'Spring' and tullips_number > 7:
            whole_bouqet -= whole_bouqet * 0.05
    elif is_holiday == 'N':
        whole_bouqet = whole_bouqet
        if season == 'Spring' and tullips_number > 7:
            whole_bouqet -= whole_bouqet * 0.05

elif season == 'Autumn' or season == 'Winter':
    hrizantemi_price = 3.75
    roses_price = 4.50
    tulips_price = 4.15
    whole_bouqet = hrizantemi_number * hrizantemi_price + roses_number * roses_price + tullips_number * tulips_price
    if is_holiday == 'Y':
        whole_bouqet += whole_bouqet * 0.15
        if season == 'Winter' and roses_number >= 10:
            whole_bouqet -= whole_bouqet * 0.1
    elif is_holiday == 'N':
        whole_bouqet = whole_bouqet
        if season == 'Winter' and roses_number >= 10:
            whole_bouqet -= whole_bouqet * 0.1

if hrizantemi_number + roses_number + tullips_number > 20:
    whole_bouqet -= whole_bouqet * 0.2

print(f'{whole_bouqet + decoration:.2f}')

