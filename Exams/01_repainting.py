nailon = int(input())
paint = int(input())
razreditel = int(input())
hours = int(input())

price_nailon = 1.50
price_paint = 14.50
price_razreditel = 5.00

total_nailon = (nailon + 2) * price_nailon
total_paint = (paint * 1.10) * price_paint
total_razreditel = razreditel * price_razreditel
torbichki = 0.4

total_materials = torbichki + total_nailon + total_paint + total_razreditel
price_maistori = total_materials * 0.3 * hours
total = total_materials + price_maistori

print(f'Total expenses: {total:.2f} lv.')