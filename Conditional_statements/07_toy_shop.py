trip = float(input())
puzzle_number = int(input())
doll_number = int(input())
teddy_bear_number = int(input())
minion_number = int(input())
truck_number = int(input())

puzzle_price = 2.60
doll_price = 3
teddy_bear_price = 4.10
minion_price = 8.20
truck_price = 2

total_toy_sum = (puzzle_number * puzzle_price) + (doll_number * doll_price) + (teddy_bear_number * teddy_bear_price) + (minion_number * minion_price) + (truck_number * truck_price)
toy_total_number = puzzle_number + doll_number + teddy_bear_number + minion_number + truck_number

if toy_total_number >= 50:
    total_toy_sum -= total_toy_sum * 0.25

rent = total_toy_sum * 0.10
profit = total_toy_sum - rent

if profit >= trip:
    print(f'Yes! {profit - trip:.2f} lv left.')
else:
    print(f'Not enough money! {trip - profit:.2f} lv needed.')