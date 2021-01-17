period = int(input())
number_patients = 0
counter_healed = 0
counter_unhealed = 0
doctors = 7

for days in range(1, period + 1):
    number_patients = int(input())
    if days % 3 == 0 and counter_unhealed > counter_healed:
        doctors = doctors + 1

    if number_patients > doctors:
        counter_healed += doctors
        counter_unhealed += number_patients - doctors
    elif number_patients <= doctors:
        counter_healed += number_patients

print(f'Treated patients: {counter_healed}.')
print(f'Untreated patients: {counter_unhealed}.')




