books = input()
counter = 0
while True:
    current_books = input()

    if current_books == 'No More Books':
        print('The book you search is not here!')
        print(f'You checked {counter} books.')
        break

    if current_books == books:
        print(f'You checked {counter} books and found it.')
        break

    counter += 1
