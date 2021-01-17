target = 10000

total = 0
while total < target:
    line = input()

    if line == 'Going home':
        steps_to_home = int(input())
        total += steps_to_home
        break
        
    steps = int(line)
    total += steps

if total < target:
    print(f'{target - total} more steps to reach goal.')
else:
    print('Goal reached! Good job!')
    print(f'{total - target} steps over the goal!')