lenght = int(input())
width = int(input())
height = int(input())
percent = float(input())

volume = height * width * lenght
liters = volume / 1000
result = liters * (1 - percent / 100)
print(result)