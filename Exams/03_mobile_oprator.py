duration = input()
contract_type = input()
mobile_net = input()
months = int(input())

monthly_fee = 0
if contract_type == 'Small':
   if duration == 'one':
       monthly_fee = 9.98
   elif duration == 'two':
       monthly_fee = 8.58
elif contract_type == 'Middle':
   if duration == 'one':
       monthly_fee = 18.99
   elif duration == 'two':
       monthly_fee = 17.09
elif contract_type == 'Large':
   if duration == 'one':
       monthly_fee = 25.98
   elif duration == 'two':
       monthly_fee = 23.59
elif contract_type == 'ExtraLarge':
   if duration == 'one':
       monthly_fee = 35.99
   elif duration == 'two':
       monthly_fee = 31.79

if mobile_net == 'yes':
    if monthly_fee <= 10:
        monthly_fee += 5.5
    elif monthly_fee <= 30:
        monthly_fee += 4.35
    elif monthly_fee > 30:
        monthly_fee += 3.85

if duration == 'two':
    monthly_fee -= monthly_fee * 0.0375

print(f'{monthly_fee * months:.2f} lv.')
