player = input()
start_points = 301
success_shot = 0
no_success_shot = 0
command = input()
while command != 'Retire':

    shot = int(input())

    if command == 'Single':
        start_points -= shot
        if start_points >= 0:
            success_shot += 1
        else:
            no_success_shot += 1
            start_points += shot
    elif command == 'Double':
        start_points -= shot * 2
        if start_points >= 0:
            success_shot += 1
        else:
            no_success_shot += 1
            start_points += shot * 2
    elif command == 'Triple':
        start_points -= shot * 3
        if start_points >= 0:
            success_shot += 1
        else:
            no_success_shot += 1
            start_points += shot * 3

    if start_points == 0:
        print(f'{player} won the leg with {success_shot} shots.')
        break

    command = input()

if command == 'Retire':
    print(f'{player} retired after {no_success_shot} unsuccessful shots.')


