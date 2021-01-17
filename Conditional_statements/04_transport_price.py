km = int(input())
type_tax = input()

fee = 0
start_fee = 0.7
if km < 20 and type_tax == 'day':
    fee = 0.79 * km + start_fee
elif km < 20 and type_tax == 'night':
    fee = 0.9 * km + start_fee
elif 20 <= km < 100:
    fee = 0.09 * km
elif km >= 100:
    fee = 0.06 * km

print(f'{fee:.2f}')