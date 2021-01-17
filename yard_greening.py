square_meters = float(input())
square_meter_price = 7.61

price = square_meters * square_meter_price
discount = (square_meters * square_meter_price * 0.18)
final_price = price - discount
print(f'The final price is {final_price} lv')
print((f'The Discount is {discount} lv'))