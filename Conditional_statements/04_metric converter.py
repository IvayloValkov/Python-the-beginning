number = float(input())
convert_from = input()
convert_to = input()

number_in_meters = 0

if convert_from == 'mm':
    number_in_meters = number / 1000
elif convert_from == 'cm':
    number_in_meters = number / 100
else:
    number_in_meters = number

result = 0
if convert_to == 'mm':
    result = number_in_meters * 1000
elif convert_to == 'cm':
    result = number_in_meters * 100
else:
    result = number_in_meters

print(f'{result:.3f}')