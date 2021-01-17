pages_count = int(input())
pages_per_hour = int(input())
days_count = int(input())

total_time = pages_count / pages_per_hour
total_hours = total_time / days_count
print(total_hours)


