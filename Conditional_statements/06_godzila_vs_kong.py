budget = float(input())
number_people = int(input())
clothes_per_person = float(input())

if number_people > 150:
    clothes_per_person = clothes_per_person * 0.90

decoration = budget * 0.10
clothes_all = number_people * clothes_per_person

if (decoration + clothes_all) > budget:
    print("Not enough money!")
    print(f"Wingard needs {(decoration + clothes_all) - budget:.2f} leva more.")
elif (decoration + clothes_all) <= budget:
    print("Action!")
    print(f"Wingard starts filming with {budget - (decoration + clothes_all):.2f} leva left.")