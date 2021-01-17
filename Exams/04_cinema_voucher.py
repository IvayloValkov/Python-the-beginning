voucher = int(input())

price = 0
ticket_counter = 0
other_counter = 0
line = input()

while True:
    if line == 'End':
        break

    if len(line) > 8:
        price = ord(line[0]) + ord(line[1])
        if voucher >= price:
            voucher -= price
        else:
            break
        ticket_counter += 1

    if len(line) <= 8:
        price = ord(line[0])
        if voucher >= price:
            voucher -= price
        else:
            break
        other_counter += 1

    line = input()

print(f'{ticket_counter}')
print(f'{other_counter}')