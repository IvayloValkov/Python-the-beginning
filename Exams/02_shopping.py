budget = float(input())
video_cards = int(input())
processors = int(input())
ram_memory = int(input())

price_video_card = 250
total_video_card = price_video_card * video_cards
price_processor = total_video_card * 0.35
total_processor = price_processor * processors
price_ram_memory = total_video_card * 0.1
total_ram_memory = price_ram_memory * ram_memory

total = total_video_card + total_processor + total_ram_memory

if video_cards > processors:
    total -= total * 0.15
diff = abs(total - budget)

if total <= budget:
    print(f'You have {diff:.2f} leva left!')
else:
    print(f'Not enough money! You need {diff:.2f} leva more!')