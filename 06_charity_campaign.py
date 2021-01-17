days_count = int(input())
bakers_count = int(input())
cakes_count = int(input())
waffles_count = int(input())
pancakes_count = int(input())

cake_price = 45
waffles_price = 5.80
pancakes_price = 3.20

money_per_day = ((cake_price * cakes_count) + (waffles_count * waffles_price) + (pancakes_count * pancakes_price)) * bakers_count
income = money_per_day * days_count
profit = income - (income * 1/8)
print(profit)
