days = int(input())
norm = 30000

working_days = 365 - days
weekend_min = days * 127
non_weekend_min = working_days * 63
total_min = weekend_min + non_weekend_min
diff = abs(total_min - norm)
hours = diff // 60
min = diff - hours * 60

if total_min >= norm:
    print(f'Tom will run away')
    print(f'{hours} hours and {min} minutes more for play')
else:
    print(f'Tom sleeps well')
    print(f'{hours} hours and {min} minutes less for play')