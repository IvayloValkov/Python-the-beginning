days = int(input())
room_type = input()
mark_type = input()

number_nights = days - 1

if room_type == 'apartment':
    price = 25
    if number_nights < 10:
      to_pay = price * number_nights * 0.70
      if mark_type == 'positive':
          to_pay += to_pay * 0.25
          print(f'{to_pay:.2f}')
      elif mark_type == 'negative':
            to_pay -= to_pay * 0.1
            print(f'{to_pay:.2f}')
    elif 10 <= number_nights <= 15:
        to_pay = price * number_nights * 0.65
        if mark_type == 'positive':
            to_pay += to_pay * 0.25
            print(f'{to_pay:.2f}')
        elif mark_type == 'negative':
            to_pay -= to_pay * 0.1
            print(f'{to_pay:.2f}')
    elif number_nights > 15:
        to_pay = price * number_nights * 0.50
        if mark_type == 'positive':
            to_pay += to_pay * 0.25
            print(f'{to_pay:.2f}')
        elif mark_type == 'negative':
            to_pay -= to_pay * 0.1
            print(f'{to_pay:.2f}')

elif room_type == 'president apartment':
    price = 35
    if number_nights < 10:
        to_pay = price * number_nights * 0.90
        if mark_type == 'positive':
            to_pay += to_pay * 0.25
            print(f'{to_pay:.2f}')
        elif mark_type == 'negative':
            to_pay -= to_pay * 0.1
            print(f'{to_pay:.2f}')
    elif 10 <= number_nights <= 15:
        to_pay = price * number_nights * 0.85
        if mark_type == 'positive':
            to_pay += to_pay * 0.25
            print(f'{to_pay:.2f}')
        elif mark_type == 'negative':
            to_pay -= to_pay * 0.1
            print(f'{to_pay:.2f}')
    elif number_nights > 15:
        to_pay = price * number_nights * 0.80
        if mark_type == 'positive':
            to_pay += to_pay * 0.25
            print(f'{to_pay:.2f}')
        elif mark_type == 'negative':
            to_pay -= to_pay * 0.1
            print(f'{to_pay:.2f}')

else:
    price = 18
    to_pay = price * number_nights
    if mark_type == 'positive':
        to_pay += to_pay * 0.25
        print(f'{to_pay:.2f}')
    elif mark_type == 'negative':
        to_pay -= to_pay * 0.1
        print(f'{to_pay:.2f}')
