hour = int(input())
week_day = input()

if 10 <= hour <= 18 and (week_day == "Monday" or week_day == 'Tuesday' or week_day == 'Wednesday' or week_day == 'Thursday' or week_day == 'Friday' or week_day == 'Saturday'):
    print('open')
else:
    print('closed')
