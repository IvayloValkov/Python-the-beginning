week_day = input()

if week_day == 'Monday' or week_day == 'Tuesday' or week_day == 'Friday':
    print('12')
elif week_day == 'Wednesday' or week_day == 'Thursday':
    print('14')
else:
    print('16')