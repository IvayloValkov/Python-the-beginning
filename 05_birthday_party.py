rent = int(input())

cake_price = rent * 0.2
drinks_price = cake_price - (cake_price * 0.45)
animator_price = rent / 3
total_price = rent + cake_price + drinks_price + animator_price
print(total_price)