rent = int(input())

statue_price = rent * 0.7
caterring_price = statue_price * 0.85
sound_price = caterring_price * 0.5

total = rent + statue_price + caterring_price + sound_price
print(f'{total:.2f}')