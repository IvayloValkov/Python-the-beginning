width = int(input())
lenght = int(input())
height = int(input())
sum_box = 0
available_space = width * lenght * height

while True:
    line = input()
    if line == 'Done':
            print(f'{available_space - sum_box} Cubic meters left.')
            break

    box_counter = int(line)
    sum_box += box_counter

    if sum_box > available_space:
        print(f'No more free space! You need {sum_box - available_space} Cubic meters more.')
        break






