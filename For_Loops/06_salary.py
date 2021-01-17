n = int(input())
salary = int(input())

for i in range(1, n + 1):
    name = input()
    if name == 'Facebook':
        salary -= 150
    elif name == 'Instagram':
        salary -= 100
    elif name == 'Reddit':
        salary -= 50

    if salary <= 0:
        print('You have lost your salary.')
        break

if salary > 0:
    print(int(salary))