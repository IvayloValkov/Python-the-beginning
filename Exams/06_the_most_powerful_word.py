word = input()
ASCII_total_values = 0

while word != 'End of words':

    for n in range(len(word)):
        ASCII_converting = ord(word[n])
        ASCII_total_values  += ASCII_converting
        

    print(ASCII_total_values)