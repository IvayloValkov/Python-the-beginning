season = input()
group = input()
students = int(input())
nights = int(input())

price = 0

if season == "Winter":
    if group == "boys" or group == "girls":
        price = 9.60
    elif group == "mixed":
        price = 10.00

elif season == "Spring":
    if group == "boys" or group == "girls":
        price = 7.20
    elif group == "mixed":
        price = 9.50

elif season == "Summer":
    if group == "boys" or group == "girls":
        price = 15.00
    elif group == "mixed":
        price = 20.00

if students >= 50:
    price -= price * 0.50

elif 20 <= students < 50:
    price -= price * 0.15

elif 10 <= students < 20:
    price -= price * 0.05

sports = ""
if season == "Winter":
    if group == "girls":
        sports = "Gymnastics"
    elif group == "boys":
        sports = "Judo"
    elif group == "mixed":
        sports = "Ski"

elif season == "Spring":
    if group == "girls":
        sports = "Athletics"
    elif group == "boys":
        sports = "Tennis"
    elif group == "mixed":
        sports = "Cycling"

elif season == "Summer":
    if group == "girls":
        sports = "Volleyball"
    elif group == "boys":
        sports = "Football"
    elif group == "mixed":
        sports = "Swimming"

final_price = price * students * nights
print(f'{sports} {final_price:.2f} lv.')