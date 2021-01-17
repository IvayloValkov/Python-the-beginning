control_value = int(input())
flag = False
counter = 0
password = ''
for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                calculation = a * b + c * d
                if calculation == control_value and a < b and c > d:
                    print(f'{a}{b}{c}{d}', end=' ')
                    counter += 1
                    if counter == 4:
                        password = 1000 * a + 100 * b + 10 * c + d
                        flag = True
print()
if flag:
    print(f'Password: {password}')
else:
    print(f'No!')
