import math

income = float(input())
grade = float(input())
min_salary = float(input())

excellent_scholarship = 0
social_scholarship = 0

if grade >= 5.50:
    excellent_scholarship += grade * 25

if grade > 4.5 and income < min_salary:
    social_scholarship += min_salary * 0.35

if social_scholarship > excellent_scholarship:
    print(f"You get a Social scholarship {math.floor(social_scholarship)} BGN")
elif excellent_scholarship >= social_scholarship:
    if excellent_scholarship != 0:
        print(f"You get a scholarship for excellent results {math.floor(excellent_scholarship)} BGN")
    else:
        print("You cannot get a scholarship!")