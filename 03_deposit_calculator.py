money = float(input())
months = int(input())
interest_rate = float(input())

interest = money * interest_rate / 100
interest_per_month = interest / 12
total_money = money + (months * interest_per_month)
print(total_money)
