days = int(input())
hours = int(input())

total_sum = 0

for day in range(1, days + 1):
    price_per_day = 0
    for hour in range(1, hours + 1):
        if day % 2 == 0 and hour % 2 != 0:
            price_per_day += 2.5
        elif day % 2 != 0 and hour % 2 ==0:
            price_per_day += 1.25
        else:
            price_per_day += 1

    total_sum += price_per_day
    print(f'Day: {day} - {price_per_day:.2f} leva')
print(f'Total: {total_sum:.2f} leva')
