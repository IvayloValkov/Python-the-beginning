target = float(input())

money_gathered = 0
while money_gathered < target:
    coctail = input()
    if coctail == 'Party!':
        print(f'We need {target - money_gathered:.2f} leva more.')
        print(f'Club income - {money_gathered:.2f} leva.')
        break
    price = len(coctail)
    number_coctails = int(input())
    price_per_coctails = price * number_coctails
    if price_per_coctails % 2 != 0:
        price_per_coctails -= price_per_coctails * 0.25
    money_gathered += price_per_coctails

    if money_gathered >= target:
        print(f'Target acquired.')
        print(f'Club income - {money_gathered:.2f} leva.')
        break



