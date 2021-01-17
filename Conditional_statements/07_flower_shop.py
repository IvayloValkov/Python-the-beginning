import math

number_magnolii = int(input())
number_zumbuli = int(input())
number_roses = int(input())
number_cactus = int(input())
gift_price = float(input())

price_magnolii = 3.25
price_zumbuli = 4
price_roses = 3.50
price_cactus = 8

total_sales = (number_magnolii * price_magnolii) + (number_zumbuli * price_zumbuli) + (number_roses * price_roses) + (number_cactus * price_cactus)
tax = total_sales * 0.05
profit = total_sales - tax


diff = abs(profit - gift_price)

if profit >= gift_price:
    print(f'She is left with {math.floor(diff)} leva.')
else:
    print(f'She will have to borrow {math.ceil(diff)} leva.')
