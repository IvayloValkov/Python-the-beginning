degrees = float(input())

if 26.00 <= degrees <= 35.00:
    print(f'Hot')
elif 20.1 <= degrees <= 25.9:
    print(f'Warm')
elif 15.00 <= degrees <= 20.00:
    print(f'Mild')
elif 12.00 <= degrees <= 14.9:
    print(f'Cool')
elif 5.00 <= degrees <= 11.9:
    print(f'Cold')
else:
    print(f'unknown')