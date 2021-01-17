import math

needed_hours = int(input())
available_days = int(input())
number_workers = int(input())

working_hours = available_days * 0.9 * 8
overtime = number_workers * 2 * available_days
total_hours = working_hours + overtime

diff = abs(math.floor(total_hours) - needed_hours)
if total_hours >= needed_hours:
    print(f'Yes!{diff} hours left.')
else:
    print(f'Not enough time!{diff} hours needed.')
