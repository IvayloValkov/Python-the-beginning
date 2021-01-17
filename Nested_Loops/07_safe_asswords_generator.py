a = int(input())
b = int(input())
password_max_count = int(input())
flag = False

for big_a in range(35, 56):
    for big_b in range(64, 97):
        for x in range(1, a + 1):
            for y in range(1, b + 1):
                print(f"{chr(big_a)}{chr(big_b)}{x}{y}{chr(big_b)}{chr(big_a)}", end="|")

                password_max_count -= 1
                big_a += 1
                big_b += 1
                if big_a > 55:
                    big_a = 35
                if big_b > 96:
                    big_b = 64

                if (x == a and y == b) or password_max_count == 0:
                    flag = True
                    break

            if flag:
                break

        if flag:
            break

    if flag:
        break