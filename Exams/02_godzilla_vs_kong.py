budget = float(input())
statisticians_count = int(input())
price_clothes = float(input())

decor_price = budget * 0.1
if statisticians_count > 150:
    price_clothes -= 0.1 * price_clothes

total = decor_price + price_clothes * statisticians_count
result = abs(total - budget)
if total > budget:
    print(f'Not enough money!')
    print(f'Wingard needs {result:.2f} leva more.')
else:
    print(f'Action!')
    print(f'Wingard starts filming with {result:.2f} leva left.')