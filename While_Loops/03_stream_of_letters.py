symbol = input()
n_appeared = False
o_appeared = False
c_appeared = False
noc = ''
word = ''

while True:
    if symbol == 'End':
        break
    first_condition = 65 <= ord(symbol) <= 90
    second_condition = 97 <= ord(symbol) <= 122

    if first_condition != second_condition:
        if symbol == 'n':
            n_appeared = True
        elif symbol == 'o':
            o_appeared = True
        elif symbol == 'c':
            c_appeared = True

        word += symbol

        if n_appeared == True and o_appeared == True and c_appeared == True:
            noc += word
            word = ''
        symbol = input()
    print(f'{word}', end='')




