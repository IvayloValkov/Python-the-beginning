chicken_menu_count = int(input())
fish_menu_count = int(input())
veggie_menu_count = int(input())


chicken_menu = 10.35
fish_menu = 12.4
veggie_menu = 8.15
delivery = 2.5

total_chicken = chicken_menu * chicken_menu_count
total_fish = fish_menu * fish_menu_count
total_veggie = veggie_menu * veggie_menu_count
total_menus = total_chicken + total_fish + total_veggie
dessert = total_menus * 0.2

print(f'Total: {total_menus + delivery + dessert:.2f}')
