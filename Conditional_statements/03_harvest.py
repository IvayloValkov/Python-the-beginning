import math

loze = int(input())
grozde_kv_m = float(input())
needed_liters = int(input())
number_workers = int(input())

total_grozde = loze * grozde_kv_m
wine = 0.4 * total_grozde / 2.5
diff = abs(wine - needed_liters)

if wine < needed_liters:
    print(f'It will be a tough winter! More {math.floor(diff)} liters wine needed.')
else:
    print(f'Good harvest this year! Total wine: {math.floor(wine)} liters.')
    print(f'{math.ceil(diff)} liters left -> {math.ceil(diff / number_workers)} liters per person.')