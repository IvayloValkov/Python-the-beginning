visitors = int(input())

counter_back = 0
counter_chest = 0
counter_legs = 0
counter_abs = 0
counter_protein_shake = 0
counter_protein_bar = 0
counter_worout = 0
counter_protein = 0
total_counter = 0

for visitor in range(1, visitors + 1):
    activity = input()

    if activity == 'Back':
        counter_back += 1
        counter_worout += 1
        total_counter += 1
    elif activity == 'Chest':
        counter_chest += 1
        counter_worout += 1
        total_counter += 1
    elif activity == 'Legs':
        counter_legs += 1
        counter_worout += 1
        total_counter += 1
    elif activity == 'Abs':
        counter_abs += 10
        counter_worout += 1
        total_counter += 1
    elif activity == 'Protein shake':
        counter_protein_shake += 1
        counter_protein += 1
        total_counter += 1
    elif activity == 'Protein bar':
        counter_protein_bar += 1
        counter_protein += 1
        total_counter += 1

print(f'{counter_back} - back')
print(f'{counter_chest} - chest')
print(f'{counter_legs} - legs')
print(f'{counter_abs} - abs')
print(f'{counter_protein_shake} - protein shake')
print(f'{counter_protein_bar} - protein bar')
print(f'{counter_worout / total_counter * 100:.2f}% - work out')
print(f'{counter_protein / total_counter * 100:.2f}% - protein')
