n = int(input())

bus_price = 0
truck_price = 0
train_price = 0
total_weight = 0
total_weight_bus = 0
total_weight_truck = 0
total_weight_train = 0
average_weight = 0
for load in range(1, n + 1):
    weight = int(input())

    if weight <= 3:
        bus_price = 200
        total_weight_bus += weight
    elif 4 <= weight <= 11:
        truck_price = 175
        total_weight_truck += weight
    elif weight >= 12:
        train_price = 120
        total_weight_train += weight

    total_weight += weight
    average_weight = (bus_price * total_weight_bus + truck_price * total_weight_truck + train_price * total_weight_train) / total_weight

print(f'{average_weight:.2f}')
print(f'{total_weight_bus / total_weight * 100:.2f}%')
print(f'{total_weight_truck / total_weight * 100:.2f}%')
print(f'{total_weight_train / total_weight * 100:.2f}%')
