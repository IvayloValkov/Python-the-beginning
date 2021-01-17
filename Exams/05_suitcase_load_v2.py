volume = float(input())
line = input()
counter = 0
while line != "End":
    suitcase = float(line)
    volume -= suitcase
    if volume <= 0:
        print("No more space!")
        break
    counter += 1
    if counter % 3 == 0:
        volume -= suitcase * 0.1
        if volume < 0:
            counter -= 1
            break
    line = input()
if line == "End":
    print("Congratulations! All suitcases are loaded!")

print(f"Statistic: {counter} suitcases loaded.")