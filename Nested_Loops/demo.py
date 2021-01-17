n = int(input())
l = int(input())
for first_symbol in range(1, n + 1):
    for second_symbol in range(1, n + 1):
        for third_symbol in range(ord("a"), (96 + l + 1)):
            for fourth_symbol in range(ord("a"), (96 + l + 1)):
                for fifth_symbol in range((max(first_symbol, second_symbol) + 1), n + 1):
                    print(f"{first_symbol}{second_symbol}{chr(third_symbol)}{chr(fourth_symbol)}{fifth_symbol}", end=' ')