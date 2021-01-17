months = int(input())

total_electricity = 0
water = 0
internet = 0
other_costs = 0

for month in range(1, months + 1):
    electricity = float(input())
    total_electricity += electricity
    water += 20
    internet += 15
    other_costs = (total_electricity + water + internet) * 1.2

print(f'Electricity: {total_electricity:.2f} lv')
print(f'Water: {water:.2f} lv')
print(f'Internet: {internet:.2f} lv')
print(f'Other: {other_costs:.2f} lv')
print(f'Average: {(total_electricity + water + internet + other_costs) / months:.2f} lv')
