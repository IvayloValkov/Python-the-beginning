import math
title = input()
seasons = int(input())
episodes = int(input())
time_per_episode = float(input())
ads = time_per_episode * 0.2
with_ads = time_per_episode + ads
total_minutes = seasons * episodes * with_ads + 10 * seasons
print(f'Total time needed to watch the {title} series is {math.ceil(total_minutes)} minutes.')