start = int(input())
end = int(input())
magical_number = int(input())
counter = 0
found_combination = False

for first_number in range(start, end + 1):
    for second_number in range(start, end + 1):
        counter += 1
        if first_number + second_number == magical_number:
            found_combination = True
            print(f'Combination N:{counter} ({first_number} + {second_number} = {magical_number})')
            break
    if found_combination == True:
        break

if found_combination == False:
    print(f'{counter} combinations - neither equals {magical_number}')