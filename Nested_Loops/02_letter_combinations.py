start_letter = ord(input())
end_letter = ord(input())
ignore_letter = ord(input())
counter = 0
for i in range(start_letter, end_letter + 1):
    if i == ignore_letter:
        continue
    for j in range(start_letter, end_letter + 1):
        if j == ignore_letter:
            continue
        for k in range(start_letter, end_letter + 1):
            if k == ignore_letter:
                continue
            counter += 1
            print(f'{chr(i)}{chr(j)}{chr(k)}', end=' ')
print(f'{counter}')

