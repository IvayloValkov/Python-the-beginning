price_skumria = float(input())
price_caca = float(input())
amount_palamud = float(input())
amount_safrid = float(input())
amount_midi = float(input())

price_palamud = price_skumria * 1.6
price_safrid = price_caca * 1.8
price_midi = 7.5

total_money = price_midi * amount_midi + price_palamud * amount_palamud + price_safrid * amount_safrid
print(f'{total_money:.2f}')