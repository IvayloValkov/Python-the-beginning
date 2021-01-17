number_bitcoin = int(input())
number_chinese = float(input())
commission = float(input())
bgn = 1

total_bitcoin = number_bitcoin * 1168
total_cny = number_chinese * 0.15 * 1.76

total_bgn = total_bitcoin + total_cny
total_eur = total_bgn / 1.95
result = total_eur - (commission/100) * total_eur

print(f'{result:.2f}')

