price_vegetable_per_kg = float(input())
price_fruit_per_kg = float(input())
kg_vegetable = int(input())
kg_fruits = int(input())

total_sales = price_fruit_per_kg * kg_fruits + price_vegetable_per_kg * kg_vegetable
total_sales_eur = total_sales / 1.94
print(f'{total_sales_eur:.2f}')
