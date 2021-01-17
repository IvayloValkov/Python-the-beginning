strawberry_price = float(input())
bananas_quantity = float(input())
oranges_quantity = float(input())
raspberry_quantity = float(input())
strawberry_quantity = float(input())

raspberry_price = strawberry_price / 2
oranges_price = raspberry_price - (raspberry_price * 0.4)
bananas_price = raspberry_price - (raspberry_price * 0.8)

total_money_need = (strawberry_price * strawberry_quantity) + (bananas_price * bananas_quantity) + (oranges_price * oranges_quantity) + (raspberry_price * raspberry_quantity)

print(total_money_need)