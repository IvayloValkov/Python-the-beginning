count1 = int(input())
count2 = int(input())
count5 = int(input())
total = int(input())

desired_sum = False

for one in range(0, count1 + 1):
    for two in range(0, count2 + 1):
        for five in range(0, count5 + 1):
            if one * 1 + two * 2 + five * 5 == total:
                print(f'{one} * 1 lv. + {two} * 2 lv. + {five} * 5 lv. = {total} lv.')
                desired_sum = True
                break

